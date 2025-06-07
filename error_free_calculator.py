#!/usr/bin/env python3
"""
Error-Free Calculator
A calculator program that demonstrates exception handling and provides
user-friendly feedback when errors occur.
"""

import logging
import os
import time

# Configure logging
logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number_input(prompt):
    """
    Get a valid number input from the user with exception handling.
    
    Args:
        prompt (str): The message to display to the user
        
    Returns:
        float: A valid number
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            logging.error("ValueError occurred: Invalid number input")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """
    Divide a by b and return the result.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: Result of division
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def display_menu():
    """Display the calculator menu."""
    print("\n===== Error-Free Calculator =====")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("================================")

def perform_calculation(choice):
    """
    Perform the calculation based on the user's choice.
    
    Args:
        choice (str): The operation choice (1-4)
        
    Returns:
        bool: True if calculation was performed, False otherwise
    """
    # Dictionary mapping choices to operations and their symbols
    operations = {
        '1': ('Addition', add, '+'),
        '2': ('Subtraction', subtract, '-'),
        '3': ('Multiplication', multiply, '*'),
        '4': ('Division', divide, '/')
    }
    
    if choice not in operations:
        return False
    
    operation_name, operation_func, operation_symbol = operations[choice]
    
    print(f"\n--- {operation_name} ---")
    
    # Get input numbers
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    
    try:
        # Perform the calculation
        result = operation_func(num1, num2)
        
        # Display the result
        print(f"\n{num1} {operation_symbol} {num2} = {result}")
        
    except ZeroDivisionError as e:
        # Handle division by zero
        print(f"\nOops! {e}.")
        logging.error(f"ZeroDivisionError occurred: {e}")
        
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"\nAn error occurred: {e}")
        logging.error(f"Unexpected error occurred: {e}")
    
    else:
        # This block executes if no exceptions occur
        print("Calculation completed successfully!")
        
    finally:
        # This block always executes
        input("\nPress Enter to continue...")
    
    return True

def main():
    """Main function to run the calculator program."""
    while True:
        clear_screen()
        display_menu()
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("\nThank you for using the Error-Free Calculator. Goodbye!")
            break
            
        elif choice in ['1', '2', '3', '4']:
            perform_calculation(choice)
            
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")
            logging.warning(f"Invalid menu choice: {choice}")
            time.sleep(1)

if __name__ == "__main__":
    main()
