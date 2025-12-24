import sys


def add_item(inventory, item_name, category, quantity):
    if item_name in inventory:
        inventory[item_name]["quantity"] += quantity
        inventory[item_name]["history"].append(f"Added {quantity}")
    else:
        inventory[item_name] = {
            "category": category,
            "quantity": quantity,
            "history": [f"Added {quantity}"]
        }


def stock_in(inventory, item_name, quantity):
    if item_name not in inventory:
        raise ValueError("Item does not exist")

    inventory[item_name]["quantity"] += quantity
    inventory[item_name]["history"].append(f"Stock in {quantity}")


def stock_out(inventory, item_name, quantity):
    if item_name not in inventory:
        raise ValueError("Item does not exist")

    if inventory[item_name]["quantity"] < quantity:
        raise ValueError("Insufficient stock")

    inventory[item_name]["quantity"] -= quantity
    inventory[item_name]["history"].append(f"Stock out {quantity}")


def low_stock_items(inventory, threshold=5):
    return {
        item: data["quantity"]
        for item, data in inventory.items()
        if data["quantity"] <= threshold
    }


if __name__ == "__main__":

    script_name = sys.argv[0]
    inventory = {}

    # Format:
    # python inventory_manager.py Pen Stationery 10 Book Education 3 Mouse Electronics 15
    if len(sys.argv) > 3 and (len(sys.argv) - 1) % 3 == 0:
        args = sys.argv[1:]
        print("User provided inventory data:")

        for i in range(0, len(args), 3):
            item = args[i]
            category = args[i + 1]
            quantity = int(args[i + 2])
            add_item(inventory, item, category, quantity)
    else:
        print("No or invalid input – using default inventory")

        add_item(inventory, "Pen", "Stationery", 10)
        add_item(inventory, "Book", "Education", 4)
        add_item(inventory, "Mouse", "Electronics", 2)

    print("\n========== Inventory Summary ==========")
    print("Script Name:", script_name)

    for item, data in inventory.items():
        print("\nItem Name:", item)
        print("Category:", data["category"])
        print("Quantity:", data["quantity"])
        print("History:", data["history"])

    print("\nLow Stock Items:", low_stock_items(inventory))
    print("======================================")
