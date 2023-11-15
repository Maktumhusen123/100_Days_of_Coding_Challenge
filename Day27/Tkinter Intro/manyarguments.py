# Pass multiple arguments and calculate the sum of all numbers passed to function using *args(Unlimited Positional Arguments, type will be tuple)
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(3, 4, 5, 6, 7)


# Multiple keyword arguments can be passed and accessed using **kwargs(type will be dictionary)
def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)


calculate(add=2, sub=3, mul=4)


# We can create our own kwargs
class Car:
    def __init__(self, **kw):
        self.color = kw.get("color")  # Using get will keep default value None if nothing is passed during initialization
        self.price = kw['price']


c1 = Car(price=30)
print(c1.color) # will print None
