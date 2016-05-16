import random

die1 = random.randint(1, 6)
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

print(total)
print ("Welcome to the dice rolling game.")

guess = int(input("Guess a roll number from 2-12 \n>"))


def start():

    if guess == int:
        if guess == total:
            print("You guessed the number! It was", total)

    else:
        print("Wrong input. Please try again.")




while (guess != total):
    print ("Your guess:", guess, "\n\
the dice rolled", total)
    start()
    break
