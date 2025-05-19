import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guess_num = random.randint(1, 100)

while True:
    user_permision = input("You Play Game 'yes' / 'no': ").lower()
    if user_permision == "yes":
        try:
            user_input = int(input("Enter your guess number between 1 and 100: "))
            if user_input < guess_num:
                print("Too low. Try again.")
                continue
            elif user_input > guess_num:
                print("Too high. Try again.")
                continue
            else:
                print(f"Congratulations! You guessed the number {guess_num} correctly!")
                break
        except ValueError:
            print("Please enter a valid number.")
        
    elif user_permision == "no":
        print("Thanks for playing the Number Guessing Game!")
        break
        