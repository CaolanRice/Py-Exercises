def bottles(num):
    for i in range(num):
        if num == 1:
            print(f'''{num} bottle of beer on the wall,\n{num} bottle of beer,\nTake one down,\nPass it around,\nNo more bottles of beer on the wall!''')
        else:
            print(f'''{num} bottles of beer on the wall,\n{num} bottles of beer,\nTake one down,\nPass it around,\n{num - 1} bottles of beer on the wall! \n''')
            num -= 1


bottles(15)
