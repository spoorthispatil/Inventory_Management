from inventory_management import add_item, low_stock_items


def test_add_item_quantity():
    inventory = {}
    add_item(inventory, "pen", "stationary", 10)
    assert inventory["pen"]["quantity"] == 10


def test_add_item_category():
    inventory = {}
    add_item(inventory, "mouse", "electronics", 5)
    assert inventory["mouse"]["category"] == "electronics"


def test_add_multiple_items():
    inventory = {}
    add_item(inventory, "pen", "stationary", 10)
    add_item(inventory, "pencil", "stationary", 3)
    assert inventory["pen"]["quantity"] == 10
    assert inventory["pencil"]["quantity"] == 3


def test_low_stock_true():
    inventory = {}
    add_item(inventory, "mouse", "electronics", 3)
    low_stock = low_stock_items(inventory)
    assert "mouse" in low_stock


def test_low_stock_false():
    inventory = {}
    add_item(inventory, "book", "stationary", 10)
    low_stock = low_stock_items(inventory)
    assert "book" not in low_stock


def test_low_stock_custom_threshold():
    inventory = {}
    add_item(inventory, "pen", "stationary", 6)
    low_stock = low_stock_items(inventory, threshold=6)
    assert "pen" in low_stock
