# Write a program that calculates the Body Mass Index from a user's height and weight.

height = float(input("Enter your height: "))
weight = int(input("Enter your weight: "))
bmi = int(weight/(height**2))

print("Your BMI = " + str(bmi))