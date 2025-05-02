import random

# Game function
def numberGuessingGame():
    # Game variables
    lifeCounter = 0
    numberRange = tuple(range(1, 101))
    numberToGuess = random.choice(numberRange)

    # Game itself
    print("Given a range of 1 - 100, guess the computer's chosen number!")
    print("Remember, you'll only have 5 lives, so make the most out of it!")
    print("The cooler you are, the closer you are!")
    while (lifeCounter < 5):
        print("Type your guess:")
        userAnswer = int(input())
        answerRange = userAnswer - numberToGuess
        answerRange = abs(answerRange)

        if answerRange == 0:
            return True
            break
        elif answerRange > 0 and answerRange <= 10:
            print("Very warm!")
        elif answerRange > 10 and answerRange <= 20:
            print("Warmer!")
        elif answerRange > 20 and answerRange <= 30:
            print("Warm!")
        elif answerRange > 30 and answerRange <= 40:
            print("Cool!")
        elif answerRange > 40 and answerRange <= 50:
            print("Cooler!")
        elif answerRange > 50:
            print("Very cool!")
        else:
            print(userAnswer, numberToGuess, userAnswer, answerRange)
            print("This should not print, there is a problem")
            return False

        lifeCounter += 1

    print("The number was: ", numberToGuess)
    return False

# Introductory prompt
print("Welcome to EspinosaJV's entertaining python game!")

while True:
    print("To start off, would you like to play? Y or N")
    userChoice = input()

    if userChoice == 'Y':
        winGame = numberGuessingGame()
        if winGame:
            print("Congratulations for guessing the correct number!")
        else:
            print("Alright, better luck next time!")
    else:
        print("Thank you for checking me out!")
        break