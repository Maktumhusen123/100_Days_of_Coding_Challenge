import random as rd

game = ["rock", "paper", "scissor"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >=3 or user_choice < 0:
    print("Invalid Choice")
else:
    print(f"User chose: {game[user_choice]}")
    computer_choice = rd.randint(0,2)
    print(f"Computer chose: {game[computer_choice]}")
    if user_choice == computer_choice :
        print("It's draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You won")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You won")
    elif computer_choice > user_choice:
        print("You lose")
