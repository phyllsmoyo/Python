# code to implement a number guessing game to return the following

"""
Guess a number between 1 and 10
Enter guess #1: 5
Your guess is too low, try again!
Enter guess #2: 8
Your guess is too high, try again!
Enter guess #3: 7
Your guess is too high, try again!
Enter guess #4: 6
You guessed it in 4 tries!
"""

import random

guess = 0
number = random.randint(1, 10)
count = 0

while guess != number:
    guess = input("Guess a number between 1 and 10: ")
    count += 1

    if guess.isnumeric():

        if guess < 1:
            print("Your guess is too low, try again!")
            continue
        elif guess > 10:
            print("Your guess is too high, try again!")
            continue
        else:
            guess = int(guess)

    else:
        print("Enter numbers only, Please!")
        continue

else:
    print(f"You guessed it in {count} tries!")
