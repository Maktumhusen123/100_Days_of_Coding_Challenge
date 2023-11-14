# Exercise 1 : create new list containing square of the following numbers of the list
numbers = [1, 1, 2, 3, 4, 5, 8]

squared_numbers = [number * number for number in numbers]
print(squared_numbers)

# Exercise 2 : Filtering Even numbers
list_of_strings = input().split(',')
# TODO 1 : Use list comprehension to convert the strings to integers
list_of_integers = [int(number) for number in list_of_strings]

# TODO 2 : Use list comprehension to filter out and store only the even numbers in result list
result = [number for number in list_of_integers if number % 2 == 0]

print(f"Even numbers from {list_of_integers} are: {result}")

# Exercise 3 : Data Overlap
# Create a list called result which contains the numbers that are common in both files.

with open("file1.txt") as file1:
    file1_numbers = file1.readlines()

with open("file2.txt") as file2:
    file2_numbers = file2.readlines()

result = [int(num) for num in file1_numbers if num in file2_numbers ]
print(result)
