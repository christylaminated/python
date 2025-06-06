# Python Assignment - Exploring the Fundamentals
# ==========================================

# Task 1 - Variables: First Python Intro
# Creating variables to describe a person
name = "Alex"
age = 25
height = 5.9

# Printing a friendly message with the variables
print(f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")

# Task 2 - Operators: Playing with Numbers
# Choosing two numbers for mathematical operations
num1 = 10  
num2 = 3   

# Addition 
print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Subtraction 
print(f"The difference between {num1} and {num2} is {num1 - num2}")

# Multiplication 
print(f"The product of {num1} and {num2} is {num1 * num2}")

# Division 
print(f"The result of dividing {num1} by {num2} is {num1 / num2}")

# Task 3 - Conditional Statements: The Number Checker

# Getting input from the user and converting it to a float
user_number = float(input("Enter a number, and I'll tell you about it: "))

# Using conditional statements to check the number
if user_number > 0:
    print("This number is positive. Awesome!")
elif user_number < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
