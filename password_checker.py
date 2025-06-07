#!/usr/bin/env python3
"""
Password Strength Checker
This program evaluates the strength of a password based on various criteria
and provides feedback to the user.
"""
import re
import string

def check_password_strength(password):
    """
    Evaluates the strength of a password and returns feedback.
    
    Args:
        password (str): The password to evaluate
        
    Returns:
        tuple: (is_strong, feedback_message, strength_score)
    """
    # Initialize feedback list and strength score
    feedback = []
    strength_score = 0
    
    # Check length
    if len(password) < 8:
        feedback.append("at least 8 characters")
    else:
        strength_score += 2
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("at least one uppercase letter")
    else:
        strength_score += 2
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        feedback.append("at least one lowercase letter")
    else:
        strength_score += 2
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        feedback.append("at least one digit")
    else:
        strength_score += 2
    
    # Check for special characters
    special_chars = set(string.punctuation)
    if not any(char in special_chars for char in password):
        feedback.append("at least one special character (like @, #, $)")
    else:
        strength_score += 2
    
    # Additional strength factors (bonus points)
    # Extra length
    if len(password) >= 12:
        strength_score += 1
    
    # Mix of character types
    char_types = 0
    if any(char.isupper() for char in password): char_types += 1
    if any(char.islower() for char in password): char_types += 1
    if any(char.isdigit() for char in password): char_types += 1
    if any(char in special_chars for char in password): char_types += 1
    if char_types >= 3:
        strength_score += 1
    
    # Cap the score at 10
    strength_score = min(strength_score, 10)
    
    # Generate feedback message
    if feedback:
        feedback_msg = "Your password needs " + ", ".join(feedback) + "."
        is_strong = False
    else:
        feedback_msg = "Your password is strong! 💪"
        is_strong = True
    
    return is_strong, feedback_msg, strength_score

def display_strength_meter(score):
    """
    Displays a visual representation of password strength.
    
    Args:
        score (int): Password strength score (0-10)
    """
    print("\nPassword Strength Meter:")
    meter = "█" * score + "░" * (10 - score)
    print(f"[{meter}] {score}/10")
    
    if score < 4:
        print("Verdict: Weak password 😟")
    elif score < 7:
        print("Verdict: Moderate password 😐")
    else:
        print("Verdict: Strong password 😄")

def main():
    """Main function to run the password checker program."""
    print("🔒 Password Strength Checker 🔒")
    print("===============================")
    print("Your password should have:")
    print("  ✓ At least 8 characters")
    print("  ✓ At least one uppercase letter")
    print("  ✓ At least one lowercase letter")
    print("  ✓ At least one digit")
    print("  ✓ At least one special character (like @, #, $)")
    print("===============================")
    
    # Get user input
    password = input("\nEnter a password: ")
    
    # Check password strength
    is_strong, feedback, score = check_password_strength(password)
    
    # Display results
    print(f"\n{feedback}")
    display_strength_meter(score)
    
    # Provide additional tips if password is weak
    if not is_strong:
        print("\nTips for a stronger password:")
        print("• Use a mix of letters, numbers, and symbols")
        print("• Make it longer (12+ characters is ideal)")
        print("• Avoid common words or patterns")

if __name__ == "__main__":
    main()
