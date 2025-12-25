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


if __name__ == "__main__":
    inventory = {}
    script_name = sys.argv[0]

   # ---------- DEFAULT VALUES ----------
default_items = "pen pencil mouse"
default_categories = "stationary stationary electronics"
default_quantities = "10 5 3"

# ---------- INPUT HANDLING ----------
if (
    len(sys.argv) == 4
    and sys.argv[1].strip()
    and sys.argv[2].strip()
    and sys.argv[3].strip()
):
    print("Using user-provided input")
    raw_items = sys.argv[1].strip()
    raw_categories = sys.argv[2].strip()
    raw_quantities = sys.argv[3].strip()
else:
    print("No / empty input provided – using DEFAULT values")
    raw_items = default_items
    raw_categories = default_categories
    raw_quantities = default_quantities

    # ---------- SPLIT INPUTS ----------
    items = raw_items.split()
    categories = raw_categories.split()
    quantities_str = raw_quantities.split()

    # ---------- DEBUG ----------
    print("\nDEBUG INPUT")
    print("Items     :", items)
    print("Categories:", categories)
    print("Quantities:", quantities_str)

    # ---------- VALIDATION ----------
    if not (len(items) == len(categories) == len(quantities_str)):
        print("ERROR: Count mismatch!")
        sys.exit(1)

    # ---------- CONVERT QUANTITIES ----------
    quantities = []
    for q in quantities_str:
        try:
            quantities.append(int(q))
        except ValueError:
            print("ERROR: Quantity must be integer ->", q)
            sys.exit(1)

    # ---------- ADD PRODUCTS ----------
    for i in range(len(items)):
        add_item(inventory, items[i], categories[i], quantities[i])

    # ---------- OUTPUT ----------
    print("\n========== INVENTORY SUMMARY ==========")
    print("Script:", script_name)

    for item, data in inventory.items():
        print("\nItem Name :", item)
        print("Category  :", data["category"])
        print("Quantity  :", data["quantity"])
        print("History   :", data["history"])

    print("\nLow Stock Items:", low_stock_items(inventory))
    print("======================================")
