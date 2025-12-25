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
    if len(sys.argv) != 4:
        print("ERROR: Expected 3 parameters")
        print("Usage:")
        print('python inventory_management.py "items" "categories" "quantities"')
        sys.exit(1)
    #Raw input from Jenkins
    raw_items = sys.argv[1].strip()
    raw_categories = sys.argv[2].strip()
    raw_quantities = sys.argv[3].strip()
    #Split inputs
    items = raw_items.split()
    categories = raw_categories.split()
    quantities_str = raw_quantities.split()
    #Debug (VERY IMPORTANT)
    print("DEBUG INPUT FROM JENKINS")
    print("Items     :", items)
    print("Categories:", categories)
    print("Quantities:", quantities_str)
    #Validation
    if not (len(items) == len(categories) == len(quantities_str)):
        print("ERROR: Count mismatch!")
        print("Items:", len(items))
        print("Categories:", len(categories))
        print("Quantities:", len(quantities_str))
        sys.exit(1)
    #Convert quantities safely
    quantities = []
    for q in quantities_str:
        try:
            quantities.append(int(q))
        except ValueError:
            print("ERROR: Quantity must be an integer ->", q)
            sys.exit(1)
    #Add unlimited products
    for i in range(len(items)):
        add_item(inventory, items[i], categories[i], quantities[i])
    print("\n========== INVENTORY SUMMARY ==========")
    print("Script:", script_name)
    for item, data in inventory.items():
        print("\nItem Name :", item)
        print("Category  :", data["category"])
        print("Quantity  :", data["quantity"])
        print("History   :", data["history"])
    print("\nLow Stock Items:", low_stock_items(inventory))
    print("======================================")