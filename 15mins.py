# use of nested for loops to
def intervals():
    for meridiem in ['am', 'pm']:
        for hour in ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
            for minutes in ['00', '15', '30', '45']:
                print(f'{hour} : {minutes} {meridiem}')


intervals()
