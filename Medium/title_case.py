import random


def getTitleCase(text):
    titledText = ''

    for i in range(len(text)):
        if i == 0:
            # first letter in every string is capitalized
            titledText += text[i].upper()
        # if the text at i is alphanumerical and the previous text was not (space or symbol), make i uppercase
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        else:
            titledText += text[i].lower()
    return titledText


assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()
