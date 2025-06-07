#!/usr/bin/env python3
"""
Functions and Recursion Assignment
This program demonstrates various concepts related to functions and recursion in Python.
"""

def task1_writing_functions():
    """Task 1: Demonstrate basic function creation and usage"""
    print("\n--- Task 1: Writing Functions ---")
    
    # Define a function that greets a user
    def greet_user(name):
        """Print a personalized greeting for the given name."""
        return f"Hello, {name}! Welcome aboard."
    
    # Define a function that adds two numbers
    def add_numbers(num1, num2):
        """Add two numbers and return the result."""
        return num1 + num2
    
    # Use the functions
    name = "Alice"
    num1, num2 = 5, 10
    
    greeting = greet_user(name)
    sum_result = add_numbers(num1, num2)
    
    print(f"{greeting} The sum of {num1} and {num2} is {sum_result}.")

def task2_default_parameters():
    """Task 2: Demonstrate functions with default parameters"""
    print("\n--- Task 2: Using Default Parameters ---")
    
    # Define a function with a default parameter
    def describe_pet(pet_name, animal_type="dog"):
        """Print a description of a pet with the given name and type."""
        return f"I have a {animal_type} named {pet_name}."
    
    # Use the function with and without the default parameter
    dog_description = describe_pet("Buddy")  # Uses default animal_type="dog"
    cat_description = describe_pet("Whiskers", "cat")  # Overrides the default
    
    print(f"{dog_description} {cat_description}")

def task3_variable_arguments():
    """Task 3: Demonstrate functions with variable arguments"""
    print("\n--- Task 3: Functions with Variable Arguments ---")
    
    # Define a function that accepts a variable number of arguments
    def make_sandwich(*ingredients):
        """Print a list of ingredients for a sandwich."""
        print("Making a sandwich with the following ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
    
    # Use the function with different numbers of arguments
    make_sandwich("Lettuce", "Tomato", "Cheese")
    
    # Example with more ingredients
    print("\nAnother sandwich:")
    make_sandwich("Turkey", "Swiss", "Mustard", "Pickles", "Onion")

def task4_recursion():
    """Task 4: Demonstrate recursive functions"""
    print("\n--- Task 4: Understanding Recursion ---")
    
    # Define a recursive function to calculate factorial
    def factorial(n):
        """Calculate the factorial of n recursively."""
        # Base case
        if n <= 1:
            return 1
        # Recursive case
        else:
            return n * factorial(n - 1)
    
    # Define a recursive function for Fibonacci sequence
    def fibonacci(n):
        """Calculate the nth number in the Fibonacci sequence recursively."""
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Recursive case
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    # Use the recursive functions
    n_factorial = 5
    n_fibonacci = 6
    
    factorial_result = factorial(n_factorial)
    fibonacci_result = fibonacci(n_fibonacci)
    
    print(f"Factorial of {n_factorial} is {factorial_result}.")
    print(f"The {n_fibonacci}th Fibonacci number is {fibonacci_result}.")
    
    # Demonstrate the Fibonacci sequence
    print("\nFibonacci sequence up to the 10th number:")
    for i in range(11):
        print(f"fibonacci({i}) = {fibonacci(i)}")

def main():
    """Main function to run all tasks"""
    print("Functions and Recursion Assignment")
    
    # Run all tasks
    task1_writing_functions()
    task2_default_parameters()
    task3_variable_arguments()
    task4_recursion()

if __name__ == "__main__":
    main()
