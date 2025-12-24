import sys


def add_item(inventory, item_name, category, quantity):
    if item_name in inventory:
        inventory[item_name]["quantity"] += quantity
    else:
        inventory[item_name] = {
            "category": category,
            "quantity": quantity,
            "history": [f"Added {quantity}"]
        }
    return inventory


def stock_in(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name]["quantity"] += quantity
        inventory[item_name]["history"].append(f"Stock in {quantity}")
    else:
        raise ValueError("Item does not exist")


def stock_out(inventory, item_name, quantity):
    if item_name not in inventory:
        raise ValueError("Item does not exist")

    if inventory[item_name]["quantity"] < quantity:
        raise ValueError("Insufficient stock")

    inventory[item_name]["quantity"] -= quantity
    inventory[item_name]["history"].append(f"Stock out {quantity}")


def get_current_quantity(inventory, item_name):
    return inventory[item_name]["quantity"]


def low_stock_items(inventory, threshold=5):
    return {
        item: details["quantity"]
        for item, details in inventory.items()
        if details["quantity"] <= threshold
    }


if __name__ == "__main__":

    script_name = sys.argv[0]
    inventory = {}

    # Expected format:
    # python inventory_manager.py item category quantity stockin stockout
    if len(sys.argv) >= 4:
        item_name = sys.argv[1]
        category = sys.argv[2]
        quantity = int(sys.argv[3])

        print("User provided inventory details:")
    else:
        item_name = "Pen"
        category = "Stationery"
        quantity = 10

        print("No input given - using default values:")

    add_item(inventory, item_name, category, quantity)

    # Sample stock movements
    stock_in(inventory, item_name, 5)
    stock_out(inventory, item_name, 3)

    print("\n========== Inventory Report ==========")
    print("Script Name:", script_name)
    print("Item Name:", item_name)
    print("Category:", inventory[item_name]["category"])
    print("Current Quantity:", inventory[item_name]["quantity"])
    print("Stock History:", inventory[item_name]["history"])
    print("Low Stock Items:", low_stock_items(inventory))
    print("=====================================")