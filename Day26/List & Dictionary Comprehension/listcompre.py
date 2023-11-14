# Traditional way of creating new list using the exisiting
numbers = [1, 2, 3]
new_list = []
for num in numbers:
  new_num = num +1
  new_list.append(new_num)


# All above mentioned code can be simplified into single line using list comprehension (pattern is [new_item for item in list]
# Example 1
num_list = [1, 2, 3, 4]
new_num_list = [num+1 for num in num_list]
print(new_num_list)

# Example 2
name = "Maktum"
letters_list = [letter for letter in name]
