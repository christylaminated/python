#!/usr/bin/env python3
"""
Exception Handling Assignment
This program demonstrates various concepts related to exceptions and error handling in Python.
"""

def task1_understanding_exceptions():
    """
    Task 1: Understanding Python Exceptions
    Demonstrates handling ZeroDivisionError and ValueError exceptions.
    """
    print("\n--- Task 1: Understanding Python Exceptions ---")
    
    while True:
        try:
            # Prompt the user for input
            user_input = input("Enter a number: ")
            
            # Try to convert input to float and divide 100 by it
            number = float(user_input)
            result = 100 / number
            
            # If no exception occurs, print the result and break the loop
            print(f"100 divided by {number} is {result}")
            break
            
        except ZeroDivisionError:
            # Handle division by zero
            print("Oops! You cannot divide by zero.")
            
        except ValueError:
            # Handle invalid numeric input
            print("Invalid input! Please enter a valid number.")

def task2_types_of_exceptions():
    """
    Task 2: Types of Exceptions
    Demonstrates raising and handling different types of exceptions.
    """
    print("\n--- Task 2: Types of Exceptions ---")
    
    # Example 1: IndexError
    try:
        # Create a list and try to access an invalid index
        my_list = [1, 2, 3]
        print(f"List: {my_list}")
        print("Trying to access index 10...")
        value = my_list[10]  # This will raise an IndexError
        
    except IndexError as e:
        # Handle the IndexError
        print(f"IndexError occurred! {e}")
        print("List index out of range.")
    
    # Example 2: KeyError
    try:
        # Create a dictionary and try to access a non-existent key
        my_dict = {"name": "Alice", "age": 25}
        print(f"\nDictionary: {my_dict}")
        print("Trying to access key 'address'...")
        address = my_dict["address"]  # This will raise a KeyError
        
    except KeyError as e:
        # Handle the KeyError
        print(f"KeyError occurred! {e}")
        print("Key not found in the dictionary.")
    
    # Example 3: TypeError
    try:
        # Try to add a string and an integer
        print("\nTrying to add string 'hello' and integer 5...")
        result = "hello" + 5  # This will raise a TypeError
        
    except TypeError as e:
        # Handle the TypeError
        print(f"TypeError occurred! {e}")
        print("Unsupported operand types.")

def task3_try_except_else_finally():
    """
    Task 3: Using try...except...else...finally
    Demonstrates the complete structure of exception handling in Python.
    """
    print("\n--- Task 3: Using try...except...else...finally ---")
    
    try:
        # Try block: Attempt to perform division
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        
    except ZeroDivisionError:
        # Except block: Handle division by zero
        print("Error: Cannot divide by zero!")
        
    except ValueError:
        # Except block: Handle invalid numeric input
        print("Error: Please enter valid numbers!")
        
    else:
        # Else block: Executes if no exceptions occur
        print(f"The result is {result}.")
        
    finally:
        # Finally block: Always executes, regardless of exceptions
        print("This block always executes.")

def main():
    """Main function to run all tasks"""
    print("Exception Handling Assignment")
    
    # Run all tasks
    task1_understanding_exceptions()
    task2_types_of_exceptions()
    task3_try_except_else_finally()

if __name__ == "__main__":
    main()
