import sys

def add_item(inventory, name, category, quantity):
    inventory[name] = {
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

def main():
    inventory = {}
    script_name = sys.argv[0]

    #DEFAULT VALUES
    default_items = ["pen", "pencil", "mouse"]
    default_categories = ["stationary", "stationary", "electronics"]
    default_quantities = [10, 5, 3]

    #HANDLING
    if len(sys.argv) != 4 or not all(sys.argv[1:]):
        print("No / empty input provided – using DEFAULT values")
        items = default_items
        categories = default_categories
        quantities = default_quantities
    else:
        items = sys.argv[1].split()
        categories = sys.argv[2].split()
        quantities_str = sys.argv[3].split()

        if not (len(items) == len(categories) == len(quantities_str)):
            print("ERROR: Count mismatch!")
            return 0   # <-- IMPORTANT (no SystemExit)

        try:
            quantities = list(map(int, quantities_str))
        except ValueError:
            print("ERROR: Quantity must be integer")
            return 0   # <-- IMPORTANT

    #INVENTORY BUILD
    for i in range(len(items)):
        add_item(inventory, items[i], categories[i], quantities[i])

    #OUTPUT
    print("\n========== INVENTORY SUMMARY ==========")
    print("Script:", script_name)

    for item, data in inventory.items():
        print("\nItem Name :", item)
        print("Category  :", data["category"])
        print("Quantity  :", data["quantity"])
        print("History   :", data["history"])

    print("\nLow Stock Items:", low_stock_items(inventory))
    print("======================================")

    return 0   
if __name__ == "__main__":
    sys.exit(main())
