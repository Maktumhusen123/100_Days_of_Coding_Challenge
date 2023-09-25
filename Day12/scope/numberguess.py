import random
EASY_TURNS = 10
HARD_TURNS = 5

def set_difficulty():
    '''Function to set difficulty'''
    difficulty = input("choose difficulty: type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def check_answer(guess, number, turns):
    if guess == number:
        print("Your guessed number is correct, You won")
    elif guess > number:
        print("Your guessed number is higher")
        return turns - 1
    elif guess < number:
        print("Your guessed number is lower")
        return turns - 1

def game():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    ran_number =random.randint(1, 100)
    print(ran_number)

    n_turns = set_difficulty()
    guess = 0
    while guess != ran_number:
        print(f"Turens left: {n_turns}")
        guess = int(input("Make a guess: "))
        n_turns = check_answer(guess, ran_number, n_turns)
        if n_turns == 0:
            print("You've run out of guesses, you lose")
            return
        elif guess != ran_number:
            print("Guess again.")

game()

