import random


def guess(number):

    random_number = random.randint(1,number)
    guess = 0

    while guess!=random_number:
        guess=int(input(f"Guess a number between 1 and {number}"))
        if guess < random_number:
            print("The guess was too low")
        elif guess > random_number:
            print("The guess was too high")

    print(f"Congrats, the guess{number} was correct")

guess(19)
