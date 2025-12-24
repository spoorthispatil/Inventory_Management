import sys


def add_item(inventory, item_name, category, quantity):
    inventory[item_name] = {
        "category": category,
        "quantity": quantity,
        "history": [f"Added {quantity}"]
    }


def low_stock_items(inventory, threshold=5):
    return {
        item: data["quantity"]
        for item, data in inventory.items()
        if data["quantity"] <= threshold
    }


if __name__ == "__main__":

    inventory = {}
    script_name = sys.argv[0]

    # Jenkins format:
    # python inventory_management.py "pen pencil mouse" "stationary stationary electronics" "20 12 11"
    if len(sys.argv) == 4:
        item_names = sys.argv[1].split()
        categories = sys.argv[2].split()
        quantities = sys.argv[3].split()

        print("User provided inventory data:")

        if not (len(item_names) == len(categories) == len(quantities)):
            print("Error: Item, category, and quantity counts must match")
            sys.exit(1)

        for i in range(len(item_names)):
            add_item(
                inventory,
                item_names[i],
                categories[i],
                int(quantities[i])
            )

    else:
        print("No input provided – using default inventory")

        add_item(inventory, "pen", "stationary", 10)
        add_item(inventory, "pencil", "stationary", 4)
        add_item(inventory, "mouse", "electronics", 2)

    print("\n========== Inventory Summary ==========")
    print("Script Name:", script_name)

    for item, data in inventory.items():
        print("\nItem:", item)
        print("Category:", data["category"])
        print("Quantity:", data["quantity"])
        print("History:", data["history"])

    print("\nLow Stock Items:", low_stock_items(inventory))
    print("======================================")
