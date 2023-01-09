import random


def mode(numbers):
    if len(numbers) == 0:
        return None

    numberCount = {}

    mostFreq = None
    mostFreqCount = 0

    for i in numbers:
        if i not in numberCount:
            numberCount[i] = 1
        else:
            numberCount[i] += 1

        if numberCount[i] > mostFreqCount:
            mostFreq = i
            mostFreqCount = numberCount[i]
    return mostFreq

    # for k, v in numberCount.items():  # loop returns only unique values in the dict
    #     if v == 1:
    #         print(k, v, sep=' : ')


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
