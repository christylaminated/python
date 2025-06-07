#!/usr/bin/env python3
"""
Recursive Artistry Program
This program demonstrates the beauty of recursion through various functions
including factorial calculation, Fibonacci sequence, and fractal patterns.
"""

import turtle
import time
import os

def clear_screen():
    """Clear the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_positive_integer(prompt):
    """
    Get a positive integer from the user with input validation.
    
    Args:
        prompt (str): The message to display to the user
        
    Returns:
        int: A positive integer
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def factorial(n):
    """
    Calculate the factorial of n recursively.
    
    Args:
        n (int): A positive integer
        
    Returns:
        int: The factorial of n (n!)
    """
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """
    Calculate the nth number in the Fibonacci sequence recursively.
    
    Args:
        n (int): A positive integer representing the position in the sequence
        
    Returns:
        int: The nth Fibonacci number
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal_tree(t, branch_length, level):
    """
    Draw a fractal tree recursively.
    
    Args:
        t (turtle.Turtle): The turtle object for drawing
        branch_length (float): Length of the current branch
        level (int): Current recursion level
    """
    # Base case: stop recursion when level reaches 0
    if level == 0:
        return
    
    # Draw the current branch
    t.forward(branch_length)
    
    # Save the current position and heading
    saved_x, saved_y = t.position()
    saved_heading = t.heading()
    
    # Right branch
    t.right(20)
    draw_fractal_tree(t, branch_length * 0.75, level - 1)
    
    # Restore position and heading
    t.penup()
    t.goto(saved_x, saved_y)
    t.setheading(saved_heading)
    t.pendown()
    
    # Left branch
    t.left(40)
    draw_fractal_tree(t, branch_length * 0.75, level - 1)
    
    # Return to the original position and heading
    t.penup()
    t.goto(saved_x, saved_y)
    t.setheading(saved_heading)
    t.pendown()

def draw_fractal_snowflake(t, length, level):
    """
    Draw a Koch snowflake fractal recursively.
    
    Args:
        t (turtle.Turtle): The turtle object for drawing
        length (float): Length of the current segment
        level (int): Current recursion level
    """
    # Base case: draw a straight line
    if level == 0:
        t.forward(length)
        return
    
    # Recursive case: replace each segment with 4 segments
    length /= 3.0
    draw_fractal_snowflake(t, length, level - 1)
    t.left(60)
    draw_fractal_snowflake(t, length, level - 1)
    t.right(120)
    draw_fractal_snowflake(t, length, level - 1)
    t.left(60)
    draw_fractal_snowflake(t, length, level - 1)

def setup_turtle():
    """
    Set up the turtle for drawing fractals.
    
    Returns:
        tuple: (screen, turtle) objects
    """
    # Create and configure the turtle screen
    screen = turtle.Screen()
    screen.title("Recursive Fractal Patterns")
    screen.bgcolor("white")
    screen.setup(width=800, height=600)
    
    # Create and configure the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.pensize(2)
    t.color("green")
    
    return screen, t

def draw_fractal_menu():
    """Display a menu for fractal selection and handle user choice."""
    clear_screen()
    print("\n--- Fractal Pattern Selection ---")
    print("1. Fractal Tree")
    print("2. Koch Snowflake")
    print("3. Return to Main Menu")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == '1':
        # Set up turtle for drawing
        screen, t = setup_turtle()
        
        # Position the turtle for the tree
        t.penup()
        t.goto(0, -250)
        t.setheading(90)  # Point upward
        t.pendown()
        
        # Get the recursion level from the user
        level = get_positive_integer("Enter the recursion level (1-6 recommended): ")
        level = min(level, 6)  # Limit to avoid excessive recursion
        
        # Draw the fractal tree
        print("\nDrawing a fractal tree... 🌳")
        draw_fractal_tree(t, 100, level)
        
        # Wait for user to close the window
        print("Close the turtle window to continue.")
        screen.exitonclick()
    
    elif choice == '2':
        # Set up turtle for drawing
        screen, t = setup_turtle()
        t.color("blue")
        
        # Position the turtle for the snowflake
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        
        # Get the recursion level from the user
        level = get_positive_integer("Enter the recursion level (1-4 recommended): ")
        level = min(level, 4)  # Limit to avoid excessive recursion
        
        # Draw the Koch snowflake (a triangle of Koch curves)
        print("\nDrawing a Koch snowflake... ❄️")
        for _ in range(3):
            draw_fractal_snowflake(t, 400, level)
            t.right(120)
        
        # Wait for user to close the window
        print("Close the turtle window to continue.")
        screen.exitonclick()
    
    elif choice == '3':
        return
    
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        draw_fractal_menu()

def display_menu():
    """Display the main menu and handle user choices."""
    while True:
        clear_screen()
        print("\n🔄 Welcome to the Recursive Artistry Program! 🔄")
        print("==============================================")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci Number")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            n = get_positive_integer("\nEnter a number to find its factorial: ")
            if n > 900:
                print("Warning: Very large factorials may cause overflow or slow computation.")
                confirm = input("Continue? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
            result = factorial(n)
            print(f"The factorial of {n} is {result}.")
            input("\nPress Enter to continue...")
        
        elif choice == '2':
            n = get_positive_integer("\nEnter the position of the Fibonacci number: ")
            if n > 35:
                print("Warning: Computing high Fibonacci numbers recursively is very slow.")
                print("This may take a long time due to the nature of recursive calculation.")
                confirm = input("Continue? (y/n): ").lower()
                if confirm != 'y':
                    continue
            
            result = fibonacci(n)
            print(f"The {n}th Fibonacci number is {result}.")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            draw_fractal_menu()
        
        elif choice == '4':
            print("\nThank you for exploring the beauty of recursion! Goodbye! 👋")
            break
        
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

def main():
    """Main function to run the recursive artistry program."""
    display_menu()

if __name__ == "__main__":
    main()
