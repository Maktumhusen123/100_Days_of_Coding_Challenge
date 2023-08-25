# Step 3

words_list = ["apple", "balloon", "carrot", "drum", "example"]

import random as rd
chosen_word = rd.choice(words_list)

#Testing code
print(f'Psst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display.append("_")
print(display)

# TO DO 1 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all letters in
# chosen_word and display has no more blanks. then you can tell the user they've won.
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter : ").lower()
    
    # check guessed letter
    for position  in range(0,len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    print(display)
    if not "_" in display:
        end_of_game = True
        print("You've won")    