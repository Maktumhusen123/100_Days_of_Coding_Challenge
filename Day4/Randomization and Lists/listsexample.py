# Lists
fruits = ["apple", "papaya", "mango", "watermelon", "pomegranate"]  # List indexing starts from 0

#print list
print(fruits)

# 0 list items using index
print(fruits[0])

# adding an element
fruits.append("Guava")      # This will append guava to the list, to add items from iterable use extend([list])
                            # TO insert an item at given position, use insert(i, item)

# removing an element
fruits.remove("apple")      # To remove an element of a specific index then use pop(), if nothing passed then last item will be removed
print(fruits)

