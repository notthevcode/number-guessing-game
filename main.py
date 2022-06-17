# __________________________Computer has a number and user needs to guess it__________________________

import random

# # For getting valid inputs from the users


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That's not a number you dumbfuck, please enter a valid number")
            continue
        else:
            break

    return value


# # creating instance variables and uning that "get_valid_integer" function
lower_limit = get_valid_integer("Enter a lower limit number: ")
upper_limit = get_valid_integer("Enter a upper limit number: ")

# Generating numbers with the user given limits
random_number = random.randint(lower_limit, upper_limit)

chances = 0

# Getting a valid input for maximum chances
while True:
    try:
        max_chances = int(input("Your chances limit: "))

    except ValueError:
        print("That's not a number you dumbfuck, please enter a valid number")
        continue
    else:
        break


while True:
    while True:
        try:
            user_number = int(input("Enter your guess number: "))
        except ValueError:
            print("That's not a number you dumbfuck, please enter a valid number")
            continue
        else:
            break
    # game over if user exceeds number of chances
    if max_chances == chances:
        print(
            f"You lost. Your chances are over {chances}/{max_chances} and the number was {random_number}")
        break
    elif user_number == random_number:
        print(
            f"You got the correct guess in {chances+1} chances and yes it was {random_number} all along.")
        break
    elif user_number < random_number:
        print(f"You have guessed too low, try again!")

    else:
        print(f"You have guessed too high, try again!")

    chances += 1

# __________________________User has a number and computer guesses it with our feedback or guidence__________________________


def computer_guess():
    low = get_valid_integer("Enter the lower limit: ")
    high = get_valid_integer("Enter the upper limit: ")
    feedback = ""
    chances = 0

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            # can be high too because low == high(see the if statement)
            guess = low
        while True:
            feedback = input(
                f"Is {guess} too high (H), too low (L), or correct (C): ")
            if feedback.lower() not in ("h", "l", "c"):
                print(
                    "That's not a valid input you dumbfuck, either H, L, C are valid inputs.")
                continue

            else:
                break
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

        chances += 1

    print(
        f"The computer guessed your number correctly in {chances} chances and it was {guess} all along.")


computer_guess()
