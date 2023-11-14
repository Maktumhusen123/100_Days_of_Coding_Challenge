# Exercise 1
# Create dictionary which takes each word in a sentence and calculate number of letters in each word.
sentence = input()
words = sentence.split()
print(words)
result = {word: len(word) for word in words}

print(result)

# Exercise 2
# Create a dictionary comprehension to convert given celsius temperature into farenheit (input will be converted to
# dictionary using eval()
weather_c = eval(input())

weather_f = {day: (temp*(9/5))+32 for (day, temp) in weather_c}

print(weather_f)
