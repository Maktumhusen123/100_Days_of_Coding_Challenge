height = int(input("Enter your height: "))
age = int(input("Enter your age: "))
if height > 120:
    print("You can ride rollercoaster")
    # nested if
    if age < 12:
        print("please pay 5$")
    #if elif statement
    elif age >= 12 and age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("You can't ride")