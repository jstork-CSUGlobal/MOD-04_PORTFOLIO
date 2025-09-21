"""
Online Shopping Cart Program
This program defines a class to represent an item in a shopping cart
the user is asked to input the details required for their 2 selected items
the program calculates the cost of both items and displays the total to the user
"""

# STEP 1: Define the class
class ItemToPurchase:
    # Constructor: sets up the default values when a new item is created
    def __init__(self):
        self.item_name = "nome"
        self.item_price = 0.0
        self.item_quantity = 0

    # Method: Cost of this item is calculated and displayed
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${total_cost:.0f}")


if __name__ == "__main__":
    # STEP 2: Gather input for two items
    items = [] # this list will hold the two ItemToPurchase objects

    # User inputs necessary details for each item desired
    for i in range(2):
        print(f"\nItem {i+1}")
        item = ItemToPurchase() # Creates a new ItemToPurchase object
        item.item_name = input("Enter Item Name:\n")
        item.item_price = float(input("Enter Item Price:\n"))
        item.item_quantity = int(input("Enter Item Quantity:\n"))

        # Completed object is added to the list
        items.append(item)

    # STEP 3: Display item costs and total
    total_cost = 0
    print("\nTOTAL COST:\n")
    for item in items:
        item.print_item_cost() # calls the class method to print this item's cost
        total_cost += item.item_price * item.item_quantity # add to total

    # Print the final total
    print(f"Total: ${int(total_cost)}")
