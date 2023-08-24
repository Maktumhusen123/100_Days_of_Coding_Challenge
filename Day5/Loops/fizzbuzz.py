# Your program should print numbers from 1 to 100, If number is divisible by 3--> Fizz, If divisible by 5--> Buzz, If both--> FizzBuzz
for number in range(1,100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number) 