name = "Maktum"
age = 24
isEligibleToVote = True

#print("My name is " + name +  " I am " + age +" Years old")  # this will throw TypeError for age as it is integer type, 
                                                            # we can concatenate only strings

# We can use f-strings
print(f"My Name is {name} and I am {age} years old. Eligible to vote: {isEligibleToVote}")