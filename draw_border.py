def drawBorder(width, height):
    if width < 2 or height < 2:
        return
    # width - 2 req due to the + on each side
    print('+' + ('-' * (width - 2)) + '+')

    for i in range(height - 2):
        print('|' + (' ' * (width - 2)) + '|')

    print('+' + ('-' * (width - 2)) + '+')


drawBorder(15, 4)
