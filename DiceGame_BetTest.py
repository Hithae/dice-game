import random
import re

bankroll = 500

print("Welcome to the dice rolling game.")
print(" ")

def startGame():

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    print(total)

    guess = ""

    print("Your bankroll: ", bankroll, "dollar")

    betChoices = ["10(1.5x payout)","20(2x payout)","30(3x payout)","40(4x payout)","50(5x payout)"]
    betChoicesStr = ' '.join(str(e) for e in betChoices)
    print("Possible bets: ",betChoicesStr)
    chosenBet = int(input("Choose your bet: "))

    if chosenBet == 10:
        chosenBet = betChoices[0]
        print("You have chosen to bet",betChoices[0],"dollars")
        print(" ")

    elif chosenBet == 20:
        chosenBet = betChoices[1]
        print("You have chosen to bet", betChoices[1],"dollars")
        print(" ")

    elif chosenBet == 30:
        chosenBet = betChoices[2]
        print("You have chosen to bet", betChoices[2],"dollars")
        print(" ")

    elif chosenBet == 40:
        chosenBet = betChoices[3]
        print("You have chosen to bet", betChoices[3],"dollars")
        print(" ")

    elif chosenBet == 50:
        chosenBet = betChoices[4]
        print("You have chosen to bet", betChoices[4],"dollars")
        print(" ")

    else:
        print("Please enter a valid bet from the given choices")
        chosenBet = int(input("Choose your bet: "))
        print("You have chosen to bet" , chosenBet, "dollars")
        print(" ")

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
            print(" ")

            playAgain = input("Would you like to play again? Y/N")

            if re.match("Y", playAgain):
                startGame()

            elif re.match("N", playAgain):
                print("Thanks for playing, till next time!")

            else:
                print("Please enter Y or N")

                playAgain = input("Would you like to play again? Y/N")

                if re.match("Y", playAgain):
                    startGame()

                elif re.match("N", playAgain):
                    print("Thanks for playing, till next time!")

        else:
            print("Better luck next time, the dice roll number was", total)

startGame()


