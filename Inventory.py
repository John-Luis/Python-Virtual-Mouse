class Inventory:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Inventory_Manager:
    def __init__(self):
        self.inventory = []  # This list needs to stay "alive"

    def add_inventory(self, item):
        self.inventory.append(item)

    def show_all_inventory(self):
        # Print the header ONCE outside the loop
        print("  Product  |  Quantity  |  Price")
        for i in self.inventory:
            # Print the actual object data inside the loop
            print(f"  {i.name:<9}|  {i.quantity:<10}|  {i.price}")


# --- CRITICAL FIX: INITIALIZE OUTSIDE THE LOOP ---
manager = Inventory_Manager()

while True:
    print(f"\nItems in list: {len(manager.inventory)}")  # Debug line
    option1 = input("What do you want to do? ").lower()

    if option1 == "add":
        product_add = input("Name: ")
        qty = int(input("Quantity: "))
        prc = int(input("Price: "))

        # Create the object and add it to the PERSISTENT manager
        new_item = Inventory(product_add, qty, prc)
        manager.add_inventory(new_item)

    elif option1 == "show":
        manager.show_all_inventory()

    elif option1 == "quit":
        break