#!/usr/bin/env python3
"""
Python Data Structures Assignment
This program demonstrates working with lists, dictionaries, and tuples in Python.
"""

def task1_working_with_lists():
    """Task 1: Demonstrate operations with lists"""
    print("\n--- Task 1: Working with Lists ---")
    
    # Create a list of favorite fruits
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"Original list: {fruits}")
    
    # Append a new fruit
    fruits.append('fig')
    print(f"After adding a fruit: {fruits}")
    
    # Remove a fruit
    fruits.remove('apple')
    print(f"After removing a fruit: {fruits}")
    
    # Print in reverse order using slicing
    reversed_fruits = fruits[::-1]
    print(f"Reversed list: {reversed_fruits}")

def task2_exploring_dictionaries():
    """Task 2: Demonstrate operations with dictionaries"""
    print("\n--- Task 2: Exploring Dictionaries ---")
    
    # Create a dictionary with personal information
    person = {
        "name": "Alice",
        "age": 25,
        "city": "Boston"
    }
    print(f"Original dictionary: {person}")
    
    # Add a new key-value pair
    person["favorite color"] = "Blue"
    print(f"After adding favorite color: {person}")
    
    # Update the city value
    person["city"] = "New York"
    print(f"After updating city: {person}")
    
    # Print all keys and values using a loop
    print("\nKeys:", end=" ")
    print(", ".join(person.keys()))
    
    print("Values:", end=" ")
    print(", ".join(str(value) for value in person.values()))
    
    # Alternative way to print keys and values
    print("\nKey-Value pairs:")
    for key, value in person.items():
        print(f"{key}: {value}")

def task3_using_tuples():
    """Task 3: Demonstrate operations with tuples"""
    print("\n--- Task 3: Using Tuples ---")
    
    # Create a tuple with favorite things
    favorites = ('Inception', 'Bohemian Rhapsody', '1984')
    print(f"Favorite things: {favorites}")
    
    # Try to change a tuple element
    try:
        print("Trying to change the first element...")
        favorites[0] = 'The Matrix'
    except TypeError as e:
        print(f"Oops! {e}")
        print("Tuples cannot be changed.")
    
    # Print the length of the tuple
    print(f"Length of tuple: {len(favorites)}")
    
    # Demonstrate tuple unpacking
    print("\nUnpacking the tuple:")
    movie, song, book = favorites
    print(f"Favorite movie: {movie}")
    print(f"Favorite song: {song}")
    print(f"Favorite book: {book}")

def main():
    """Main function to run all tasks"""
    print("Python Data Structures Assignment")
    
    # Run all tasks
    task1_working_with_lists()
    task2_exploring_dictionaries()
    task3_using_tuples()

if __name__ == "__main__":
    main()
