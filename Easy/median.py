import random


def median(numbers):
    if len(numbers) == 0:
        return None

    numbers.sort()
    mid_index = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[mid_index]
    else:
        return (numbers[mid_index] + numbers[mid_index - 1]) / 2


assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
    random.shuffle(testData)
    assert median(testData) == 6
