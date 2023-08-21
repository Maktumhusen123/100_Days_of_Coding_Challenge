# Write a program that interprets BMI based on user's weight and height
# If BMI is under 18.5 --> underweight, over 18.5 but below 25 --> normal
# over 25 but below 30 --> overweight, over 30 but below 35 --> obese, above 35 --> clinically obese
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight/(height**2)

# and  or not are logical operators
if bmi <= 18.5 :
    print("You are underweight")
elif bmi > 18.5 and bmi < 25:
    print("Your are Normal")
elif bmi >= 25 and bmi < 30:
    print("You are overweight")
elif bmi >= 30 and bmi < 35:
    print("You are obese")
else:
    print("You are medically obese")