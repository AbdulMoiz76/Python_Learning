import random

while True:

    Choice = input(
        "Do you wnat to play a dice rolling game? (yes/no):  ").lower()
    if Choice == "yes":
        print("Welcome to the Dice Rolling Game!")
        dice_roll_1 = random.randint(1, 6)
        dice_roll_2 = random.randint(1, 6)
        print(f"You rolled a {dice_roll_1} and a {dice_roll_2}")
    elif Choice == "no":
        print("You have Play Game just FUN! ")
        continue
    elif Choice == "quit".lower():
        print("Thanks for playing the Dice Rolling Game!")
        break
    else:
        print("Please enter valid input (yes/no)")
        continue
