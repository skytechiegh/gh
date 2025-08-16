# Guess the Number Game
import random

def guess_the_number():
    print("=== Guess the Number Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(f"\nEnter your guess (attempt {attempts + 1}/{max_attempts}): "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret_number}!")
                return True
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as an attempt
    
    print(f"\n😔 Game Over! You ran out of attempts.")
    print(f"The number was {secret_number}.")
    return False

def play_again():
    while True:
        response = input("\nWould you like to play again? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Main game loop
def main():
    print("Welcome to Guess the Number!")
    
    while True:
        guess_the_number()
        
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()