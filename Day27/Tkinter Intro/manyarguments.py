# Pass multiple arguments and calculate the sum of all numbers passed to function using *args(Unlimited Positional Arguments)
def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)


add(3, 4, 5, 6, 7)

