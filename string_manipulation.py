"""
String Manipulation Assignment
This program demonstrates various string operations including slicing, 
string methods, and checking for palindromes.
"""

def task1_string_slicing():
    """Task 1: Demonstrate string slicing and indexing"""
    print("\n--- Task 1: String Slicing and Indexing ---")
    
    # Create a string variable
    my_string = "Python is amazing!"
    
    # Extract using slicing
    first_word = my_string[:6]
    amazing_part = my_string[10:17]
    reversed_string = my_string[::-1]
    
    # Print with labels
    print(f"Original string: {my_string}")
    print(f"First word: {first_word}")
    print(f"Amazing part: {amazing_part}")
    print(f"Reversed string: {reversed_string}")

def task2_string_methods():
    """Task 2: Demonstrate various string methods"""
    print("\n--- Task 2: String Methods ---")
    
    # Create a string with extra spaces
    my_string = " hello, python world! "
    print(f"Original string: '{my_string}'")
    
    # Apply string methods
    stripped = my_string.strip()
    capitalized = stripped.capitalize()
    replaced = stripped.replace("world", "universe")
    uppercase = stripped.upper()
    
    # Print results
    print(f"After strip(): '{stripped}'")
    print(f"After capitalize(): '{capitalized}'")
    print(f"After replace('world', 'universe'): '{replaced}'")
    print(f"After upper(): '{uppercase}'")

def task3_palindrome_checker():
    """Task 3: Check if a string is a palindrome"""
    print("\n--- Task 3: Palindrome Checker ---")
    
    # Get user input
    word = input("Enter a word: ")
    
    # Remove spaces and convert to lowercase for better comparison
    cleaned_word = word.lower().replace(" ", "")
    
    # Check if it's a palindrome using slicing
    reversed_word = cleaned_word[::-1]
    
    # Compare and print result
    if cleaned_word == reversed_word:
        print(f"Yes, '{word}' is a palindrome!")
    else:
        print(f"No, '{word}' is not a palindrome.")

def main():
    """Main function to run all tasks"""
    print("String Manipulation Assignment")
    
    # Run all tasks
    task1_string_slicing()
    task2_string_methods()
    task3_palindrome_checker()

if __name__ == "__main__":
    main()
