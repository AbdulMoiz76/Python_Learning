import random


choice =("r","p","s")
emoji = {
    "r": "✊",
    "p": "✋",
    "s": "✌️"
}

while True:
    user_choice = input("Rock, Paper,Scissor? (r/p/s): ").lower()

    if user_choice not in choice:
        print("Invalid choice, please try again.")
        continue
    else:
        print(f"you choose the {emoji[user_choice]}")


    computer_choice = random.choice(choice)
    print(f"Computer Choose the {emoji[computer_choice]}") 

    if (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        print("You win!")
    elif user_choice == computer_choice:
        print("Its a tie!")
    else:
        print("You Lose! Better luck next time.")
    user_permision = input("Do you want to play again? (yes/no): ").lower()
    if user_permision == "yes":
        continue
    else:
        print("Thanks for playing Rock, Paper, Scissor!")
        break


