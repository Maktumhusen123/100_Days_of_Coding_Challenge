# Pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?: ")  #small = 15$, medium = 20$, large = 25$
add_pepperoni = input("Do you want pepporoni? Y or N: ") #pepporoni small = +2$ medium or large = +3$
extra_cheese = input("Do you want extra cheese? Y or N: ") # cheese all = +1$

bill = 0

if size == "S":
    bill += 15    
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is {bill}")