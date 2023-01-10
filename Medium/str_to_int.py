def convertStrToInt(stringNum):

    STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3,
                  '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    if stringNum[0] == '-':
        isNegative = True
        stringNum = stringNum[1:]  # removes the - sign
    else:
        isNegative = False

    integerNum = 0  # variable to store the converted number starts at 0, so when multiplied by 10 the number stays the same as it's digit after addition
    for i in range(len(stringNum)):
        digit = STR_TO_INT[stringNum[i]]
        # multiplying by 10 moves all of the digits left by 1 place
        integerNum = (integerNum * 10) + digit

    if isNegative:
        return -integerNum
    else:
        return integerNum


for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
