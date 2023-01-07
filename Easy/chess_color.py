#on a chess board, a square is white if the row and column are both even or both odd
#otherwise the square is black

def getChessSquareColor(column, row):
    if column > 8 or row > 8 or column < 1 or row < 1:
        return ""
    elif column % 2 == row % 2:
        return 'white'
    else:
        return 'black'


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
