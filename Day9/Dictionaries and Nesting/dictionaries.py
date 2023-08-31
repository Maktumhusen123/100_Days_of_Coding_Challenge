# Dictionaries : key value pairings
# Creating dictionary   {key: value}  Eg: {"Bug": "An error in a program"}

programming_dictionary = {
    "Bug": "An error in a program that prevents program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
}
#print(programming_dictionary)

# Retreiving of an item from dictionary : vaues can be accessed using keys
print(programming_dictionary["Function"])

# Adding new entry to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

empty_dictionary = {}

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Editing an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

for key in programming_dictionary:
    print(f"Key:{key}")    # Keys will be printed
    print(f"value: {programming_dictionary[key]}")    # values will be printed
