import random

print("Welcome to the dice rolling game.")

def startGame():

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    print(total)

    guess = ""

    while guess != total:

        try:
            guess = int(input("Guess a roll number from 2-12 \n>"))

        except:
            print("Please enter an integer between 2-12")
            guess = int(input("Guess a roll number from 2-12 \n>"))
            break

    if guess >= 2 and guess <= 12:

        if guess == total:

            print("You guessed the number! It was", total)
            playAgain = input("Would you like to play again? Y/N")

            if playAgain == "Y" or "y":
                startGame()

            elif playAgain == "N" or "n":
                print("Thanks for playing, till next time!")

            else:
                print("Please enter Y or N")
        else:
            print("Better luck next time, the dice roll number was", total)

startGame()



