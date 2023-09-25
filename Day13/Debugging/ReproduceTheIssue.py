from random import randint
dice = [1, 2, 3, 4, 5, 6]
guess = randint(1, 6)
print(dice[guess])

# The above code may produce a bug(error) i.e. list index out of range sometimes(can be tested by reproducing the issue)
# How can be fixed?
from random import randint
dice = [1, 2, 3, 4, 5, 6]
guess = randint(0, 5)
print(dice[guess])
