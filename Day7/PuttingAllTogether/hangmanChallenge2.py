# Step 2

words_list = ["apple", "balloon", "carrot", "drum", "example"]

import random as rd
chosen_word = rd.choice(words_list)

#Testing code
print(f'Psst, the solution is {chosen_word}.')

# TO DO 1 - Create an empty list called display. For each letter in chosen_word, add a _ to display.
# SO if the chosen_word was apple, display should be ["_","_","_","_","_"] with 5 _ representing each letter to guess
display = []
for letter in chosen_word:
    display.append("_")
print(display)

guess = input("Guess a letter : ").lower()

# TO DO 2 - Loop through each position in the chosen_word; If the letter at that position matches guess then reveal that
# letter in the display at that position. e.g If the user guessed "p" and the chosen word was "apple" then display should be
# ["_", "p", "p", "_","_"]
for position  in range(0,len(chosen_word)):
    if guess == chosen_word[position]:
        display[position] = guess

# TO DO 3 - Print display and you should see the guessed letter in the corect position and every other letter replaced with _
print(display)     