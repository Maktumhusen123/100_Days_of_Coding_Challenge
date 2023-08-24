list_of_scores = input("Enter list of scores: ").split()

# converting string list to int list
for score in range(0,len(list_of_scores)):
    list_of_scores[score] = int(list_of_scores[score])

highest_score = 0
for score in list_of_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is {highest_score}")