import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SPECIAL_CHARS = '~!@#$%^&*()_+'
NUMBERS = '1234567890'

ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + SPECIAL_CHARS + NUMBERS


def generatePassword(length):
    if length < 12:
        length = 12

    password = []

    # make sure that each generated password has at least 1 of each category first
    password.append(LOWER_LETTERS[random.randint(0, 25)])
    password.append(UPPER_LETTERS[random.randint(0, 25)])
    password.append(SPECIAL_CHARS[random.randint(0, 12)])
    password.append(NUMBERS[random.randint(0, 9)])

    while len(password) < length:
        password.append(ALL_CHARS[random.randint(0, 71)])

    random.shuffle(password)

    # join all of the strings in the pw list into one string
    return ''.join(password)


# print(generatePassword(15))
assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL_CHARS:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
