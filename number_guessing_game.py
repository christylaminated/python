# Number Guessing Game 

import random

def play_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Variables to track attempts and game state
    attempts = 0
    max_attempts = 10
    guessed_correctly = False
    
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it!")
    
    # Step 2: Use a while loop for the guessing process
    while attempts < max_attempts and not guessed_correctly:
        # Get user's guess
        try:
            guess = int(input("\nGuess the number (between 1 and 100): "))
            attempts += 1
            
            # Step 3: Check the guess against the random number
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                # Don't count invalid guesses
                attempts -= 1
            elif guess < number_to_guess:
                print("Too low! Try again. ")
                print(f"Attempts remaining: {max_attempts - attempts}")
            elif guess > number_to_guess:
                print("Too high! Try again. ")
                print(f"Attempts remaining: {max_attempts - attempts}")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed it in {attempts} {'attempt' if attempts == 1 else 'attempts'}! 🎉")
        
        except ValueError:
            print("Please enter a valid number!")
            # Don't count invalid inputs
            attempts -= 1
    
    # Game over if max attempts reached
    if not guessed_correctly:
        print(f"\n😔 Game over! The number was {number_to_guess}. Better luck next time! 😔")
    
    # Ask if the player wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again.startswith('y'):
        play_guessing_game()
    else:
        print("Thanks for playing! See you next time! 👋")

# Start the game
if __name__ == "__main__":
    play_guessing_game()
