def convertIntToStr(integerNum):
    if integerNum == 0:
        return '0'

    INT_TO_STR = {}

    for i in range(10):
        # populate dict with digits and their string values
        INT_TO_STR[i] = str(i)

    if integerNum < 0:
        isNegative = True
        # if the passed integer is negative, make it positive, will add a - sign at the end
        integerNum = -integerNum
    else:
        isNegative = False

    stringNum = ''
    while integerNum > 0:
        lastPlaceDigit = integerNum % 10  # evaluates to lastdigit of integer num
        stringNum = INT_TO_STR[lastPlaceDigit] + \
            stringNum  # adding the last digit to the string
        integerNum //= 10

    if isNegative:
        # if the int was initially negative, return the string with a - in front
        return '-' + stringNum
    else:
        return stringNum


for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
