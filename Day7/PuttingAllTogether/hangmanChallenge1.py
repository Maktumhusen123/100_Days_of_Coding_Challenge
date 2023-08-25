# Step 1

words_list = ["apple", "balloon", "carrot", "drum", "example"]

# TO DO 1 - Randomly choose a word from the words_list and assign it to a variable called chosen_word
import random as rd
chosen_word = rd.choice(words_list)

#print(chosen_word)

# TO DO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess = input("Guess a letter : ").lower()

# TO DO 3 - check if the letter the user guessed is one of the letters in the chosen_word
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
        