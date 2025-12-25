import pytest
from inventory_management import add_item, low_stock_items


def test_add_single_item():
    inventory = {}
    add_item(inventory, "pen", "stationary", 10)

    assert "pen" in inventory
    assert inventory["pen"]["category"] == "stationary"
    assert inventory["pen"]["quantity"] == 10
    assert inventory["pen"]["history"] == ["Added 10"]


def test_add_multiple_items():
    inventory = {}

    add_item(inventory, "pen", "stationary", 10)
    add_item(inventory, "mouse", "electronics", 3)
    add_item(inventory, "book", "stationary", 7)

    assert inventory["pen"]["quantity"] == 10
    assert inventory["mouse"]["quantity"] == 3
    assert inventory["book"]["quantity"] == 7


def test_low_stock_default_threshold():
    inventory = {}

    add_item(inventory, "pen", "stationary", 10)
    add_item(inventory, "mouse", "electronics", 3)
    add_item(inventory, "keyboard", "electronics", 2)

    low_stock = low_stock_items(inventory)

    assert "mouse" in low_stock
    assert "keyboard" in low_stock
    assert "pen" not in low_stock


def test_low_stock_custom_threshold():
    inventory = {}

    add_item(inventory, "pen", "stationary", 6)
    add_item(inventory, "book", "stationary", 4)

    low_stock = low_stock_items(inventory, threshold=6)

    assert "pen" in low_stock
    assert "book" in low_stock


def test_empty_inventory():
    inventory = {}
    low_stock = low_stock_items(inventory)

    assert low_stock == {}
