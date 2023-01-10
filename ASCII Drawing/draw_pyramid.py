def drawPyramid(height):
    for rowNumber in range(height):
        spacesRequired = ' ' * (height - (rowNumber + 1))
        pyramidHash = '#' * (rowNumber * 2 + 1)
        print(spacesRequired + pyramidHash)


drawPyramid(5)
