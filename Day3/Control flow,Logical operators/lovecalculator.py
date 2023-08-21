print("Welcome to the Love calculator")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_name = name1 + name2
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
love = l + o + v + e

love_score = true + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
