def checkPrime(number):
    for i in range(2,number):
        if number % i == 0:
            print(f"The {number} is not prime number.")
            break
        else:
            print(f"The {number} is prime number.")
            break

num = int(input("Enter Number: "))
checkPrime(number=num)
