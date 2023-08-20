print("Welcome to the tip calculator")
bill = int(input("What was the bill? Rs."))
tip_percentage = int(input("What percentage tip you would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill -= ( bill * (tip_percentage/100) )
#print(bill)
share_bill = bill / people
#print(share_bill)
print(f"Each person should pay: {share_bill}")
