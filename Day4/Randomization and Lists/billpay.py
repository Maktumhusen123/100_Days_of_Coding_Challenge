import random as rd

names_string = input("Give me everybody's names, separated by comma. ")
names = names_string.split(",")
print(names)

choice = rd.randint(0,len(names)-1)     # instead you can also use choice()

print(f"{names[choice]} is going to buy the meal today!")