#return a string of a given number along with it's ordinal suffix


def ordinalSuffix(number):
    strNumber = str(number)
    if strNumber[-2:] in ('11', '12', '13'):
        return strNumber + 'th'
    elif strNumber[-1] == '1':
        return strNumber + 'st'
    elif strNumber[-1] == '2':
        return strNumber + 'nd'
    elif strNumber[-1] == '3':
        return strNumber + 'rd'
    else:
        return strNumber + 'th'


assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'


#alternate method using modulo to compare integers instead of strings

def moduloSuffix(number):
    if number % 100 in (11, 12, 13):
        return str(number) + 'th'
    if number % 10 == 1:
        return str(number) + 'st'
