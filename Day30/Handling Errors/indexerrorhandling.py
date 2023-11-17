fruits = eval(input())


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"there is no fruit at index {index}")
    else:
        print(fruit + " pie")


make_pie(4)
