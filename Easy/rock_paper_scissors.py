def rpsWinner(player1, player2):
    if player1 == 'rock' and player2 == 'paper':
        return 'player two wins'
    elif player1 == 'rock' and player2 == 'scissors':
        return 'player one wins'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player one wins'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'player two wins'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'player two wins'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'player one wins'
    else:
        return 'it\'s a tie'


assert rpsWinner('rock', 'paper') == 'player two wins'
assert rpsWinner('rock', 'scissors') == 'player one wins'
assert rpsWinner('paper', 'scissors') == 'player two wins'
assert rpsWinner('paper', 'rock') == 'player one wins'
assert rpsWinner('scissors', 'rock') == 'player two wins'
assert rpsWinner('scissors', 'paper') == 'player one wins'
assert rpsWinner('rock', 'rock') == 'it\'s a tie'
assert rpsWinner('paper', 'paper') == 'it\'s a tie'
assert rpsWinner('scissors', 'scissors') == 'it\'s a tie'
