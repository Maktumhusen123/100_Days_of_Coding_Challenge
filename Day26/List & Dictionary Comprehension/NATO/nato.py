import pandas
data = pandas.read_csv("nato.csv")

# TODO 1 : Create a dictionary in the format {"A": "Alfa"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)

# TODO 2 : Create a list of the phonetic code words from a word that user inputs
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
