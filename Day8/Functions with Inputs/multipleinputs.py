def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#greet_with("Akbar","Belgaum")

# what if i switch order?, these are Positional arguments. How to avoid this?
#greet_with("Belgaum","Akbar")

# Use Keyword Arguments
greet_with(location="Belaum", name="Akbar")