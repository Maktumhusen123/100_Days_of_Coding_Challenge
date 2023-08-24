import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print("Welcome to the Password Generator")
letters_count = int(input("How many letters would you like in your password?: "))
symbols_count = int(input("How many symbols would you like in your password?: "))
numbers_count = int(input("How many numbers would you like in your password?: "))
# Hard Level : Random order
password_list = []

for char in range(1, letters_count + 1):
    password_list.append(rd.choice(letters))

for char in range(1, symbols_count + 1):
    password_list.append(rd.choice(symbols))

for char in range(1, numbers_count + 1):
    password_list.append(rd.choice(numbers))
#print(password_list)
rd.shuffle(password_list)      # change the order of a list
#print(password_list)
password = ""
for char in password_list:
    password += char

print(password)
