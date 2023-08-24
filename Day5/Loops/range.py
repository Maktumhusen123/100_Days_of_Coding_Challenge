# Range function : range(start, stop, step). step is optional, if not specified will be considered as 1.
# excluding stop, it will iterate till stop-1. Eg: below code prints numbers from 1 to 9 not 10.
for number in range(1,10):
    print(number)

# Adding Even number Exercise
sum = 0
for number in range(2,101,2):
    if number % 2 == 0:
        sum += number
print(f"Sum of all even numbers is : {sum}")