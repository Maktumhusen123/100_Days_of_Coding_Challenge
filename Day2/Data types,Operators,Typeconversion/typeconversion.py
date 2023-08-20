# type() function will return type of data stored in variable or object
print(type(2))
print(type(2.3456))
print(type("Hello"))
print(type(True))

print("------------------------------------------------")
num = len("Maktum")   # num = 6 is an Integer
print(type(num))
print(type(str(num)))        # Conversion of one data type to another is called Typecasting(Type conversion), 
                             # Here num is converted string

print("-------------------------------------------------")
print("Exercise")
# Exercise
# Given a two digit number, print the sum of two digits
number = input("Enter a two digit number: ")
sum = int(number[0]) + int(number[1])
print(sum)