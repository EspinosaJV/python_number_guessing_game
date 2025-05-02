import random

# constant variables
MAX_LIVES = 5
MIN_NUMBER = 1
MAX_NUMBER = 100

# player feedback each guess
def get_feedback(diff):
    if diff == 0:
        return "Correct!"
    elif diff <= 10:
        return "Very warm!"
    elif diff <= 20:
        return "Warmer!"
    elif diff <= 30:
        return "Warm!"
    elif diff <= 40:
        return "Cool!"
    elif diff <= 50:
        return "Cooler!"
    else:
        return "Very cool!"

# game functionality
def number_guessing_game():
    number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)
    lives = 0

    print(f"\nGuess the number between {MIN_NUMBER} and {MAX_NUMBER}!")
    print(f"You have {MAX_LIVES} lives. Good luck!\n")

    while lives < MAX_LIVES:
        try:
            user_input = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        diff = abs(user_input - number_to_guess)
        feedback = get_feedback(diff)

        print(feedback)

        if diff == 0:
            return True

        lives += 1
        print(f"Lives left: {MAX_LIVES - lives}\n")

    print(f"Game over! The number was: {number_to_guess}")
    return False

# Game entry point
def main():
    print("Welcome to EspinosaJV's number guessing game!")

    while True:
        user_choice = input("Would you like to play? (Y/N): ").strip().lower()
        if user_choice == 'y':
            won = number_guessing_game()
            if won:
                print("Congratulations, you guessed it right!")
            else:
                print("Well, better luck next time!")
        elif user_choice == 'n':
            print("Alright, thanks for playing!")
            break
        else:
            print("Please only choose from 'Y' or 'N'.")

if __name__ == "__main__":
    main()