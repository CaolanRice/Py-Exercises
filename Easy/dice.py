import random


def rollDice(numberOfDice):
    total = 0
    for i in range(1, numberOfDice + 1):
        total += random.randint(1, 6)
    return total


assert rollDice(0) == 0
# insurance that two 1000 dice rolls don't end up the same
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600
