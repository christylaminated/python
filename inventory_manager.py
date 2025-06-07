
"""
Inventory Management System
This program demonstrates a simple inventory management system using dictionaries and tuples.
"""

def display_inventory(inventory):
    """
    Display all items in the inventory in a formatted way.
    
    Args:
        inventory (dict): The inventory dictionary
    """
    print("\nCurrent inventory:")
    if not inventory:
        print("Inventory is empty!")
        return
    
    for item, details in inventory.items():
        quantity, price = details
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

def add_item(inventory, item_name, quantity, price):
    """
    Add a new item to the inventory.
    
    Args:
        inventory (dict): The inventory dictionary
        item_name (str): Name of the item
        quantity (int): Quantity of the item
        price (float): Price per unit
    
    Returns:
        dict: Updated inventory
    """
    if item_name in inventory:
        print(f"{item_name} already exists in inventory. Use update function instead.")
        return inventory
    
    inventory[item_name] = (quantity, price)
    print(f"Added {item_name} to inventory.")
    return inventory

def remove_item(inventory, item_name):
    """
    Remove an item from the inventory.
    
    Args:
        inventory (dict): The inventory dictionary
        item_name (str): Name of the item to remove
    
    Returns:
        dict: Updated inventory
    """
    if item_name in inventory:
        del inventory[item_name]
        print(f"Removed {item_name} from inventory.")
    else:
        print(f"{item_name} not found in inventory.")
    
    return inventory

def update_item(inventory, item_name, quantity=None, price=None):
    """
    Update quantity or price of an existing item.
    
    Args:
        inventory (dict): The inventory dictionary
        item_name (str): Name of the item to update
        quantity (int, optional): New quantity. If None, keeps original value.
        price (float, optional): New price. If None, keeps original value.
    
    Returns:
        dict: Updated inventory
    """
    if item_name not in inventory:
        print(f"{item_name} not found in inventory. Use add function instead.")
        return inventory
    
    current_quantity, current_price = inventory[item_name]
    
    # Update only the provided values
    new_quantity = quantity if quantity is not None else current_quantity
    new_price = price if price is not None else current_price
    
    inventory[item_name] = (new_quantity, new_price)
    print(f"Updated {item_name} in inventory.")
    
    return inventory

def calculate_total_value(inventory):
    """
    Calculate the total value of all items in the inventory.
    
    Args:
        inventory (dict): The inventory dictionary
    
    Returns:
        float: Total value of inventory
    """
    total_value = 0
    
    for item, details in inventory.items():
        quantity, price = details
        item_value = quantity * price
        total_value += item_value
    
    return total_value

def main():
    """Main function to run the inventory management program."""
    print("🛒 Welcome to the Inventory Manager! 🛒")
    
    # Start with an empty inventory
    inventory = {}
    
    # Add initial items
    inventory = add_item(inventory, "apple", 10, 2.5)
    inventory = add_item(inventory, "banana", 20, 1.2)
    
    # Display initial inventory
    display_inventory(inventory)
    
    # Add a new item
    print("\nAdding a new item: mango")
    inventory = add_item(inventory, "mango", 15, 3.0)
    
    # Display updated inventory
    display_inventory(inventory)
    
    # Update an item
    print("\nUpdating quantity of apples to 15")
    inventory = update_item(inventory, "apple", quantity=15)
    
    # Display updated inventory
    display_inventory(inventory)
    
    # Remove an item
    print("\nRemoving bananas from inventory")
    inventory = remove_item(inventory, "banana")
    
    # Display updated inventory
    display_inventory(inventory)
    
    # Calculate and display total value
    total_value = calculate_total_value(inventory)
    print(f"\nTotal value of inventory: ${total_value:.2f}")
    
    print("\n--- Interactive Mode ---")
    print("Let's try some operations interactively!")
    
    while True:
        print("\nChoose an operation:")
        print("1. Display inventory")
        print("2. Add new item")
        print("3. Remove item")
        print("4. Update item")
        print("5. Calculate total value")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            display_inventory(inventory)
        
        elif choice == "2":
            item_name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: $"))
                inventory = add_item(inventory, item_name, quantity, price)
            except ValueError:
                print("Invalid input. Quantity must be an integer and price must be a number.")
        
        elif choice == "3":
            item_name = input("Enter item name to remove: ")
            inventory = remove_item(inventory, item_name)
        
        elif choice == "4":
            item_name = input("Enter item name to update: ")
            if item_name in inventory:
                try:
                    update_choice = input("Update quantity, price, or both? (q/p/b): ").lower()
                    
                    if update_choice in ['q', 'b']:
                        quantity = int(input("Enter new quantity: "))
                    else:
                        quantity = None
                        
                    if update_choice in ['p', 'b']:
                        price = float(input("Enter new price: $"))
                    else:
                        price = None
                        
                    inventory = update_item(inventory, item_name, quantity, price)
                except ValueError:
                    print("Invalid input. Quantity must be an integer and price must be a number.")
            else:
                print(f"{item_name} not found in inventory.")
        
        elif choice == "5":
            total_value = calculate_total_value(inventory)
            print(f"Total value of inventory: ${total_value:.2f}")
        
        elif choice == "6":
            print("Thank you for using the Inventory Manager. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
