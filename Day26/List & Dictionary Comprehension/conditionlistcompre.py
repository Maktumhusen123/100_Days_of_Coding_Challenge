names = ["Maktum", "Akbar", "Hanip", "Ullas", "Shahid", "Abdul", "Rahul"]

# We can do conditional list comprehension(pattern is : [new_item for item in list if condition]
short_names = [name for name in names if len(name) < 6]
print(short_names)
