# making a random number guessing game

import random

# r = random.randint(0, 4)

# print(r)


flag = True

while flag:
    num = input("Enter the upper bound: ")

    if num.isdigit():
        print("Let's play!")
        num = int(num)
        flag = False
    else:
        print("Invalid input!")

secret_number = random.randint(1, num)

guess = None
count = 1

while guess != secret_number:
    guess = input("Please type a number between 1 and " + str(num) + ": ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret_number:
        print("You got it!")
    else:
        print("Please try again!")
        count += 1


print(f"It took you {count} guesses.")
