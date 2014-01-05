import random

def generate_quote(symbol):
    '''
        return the winning quote for symbols: 
            r -- rock,
            p -- paper,
            s -- scissors
    '''
    QUOTES = {
        'r' : 'Rock smashes scissors!!!',
        'p' : 'Paper covers rock!!',
        's' : 'Scissors cuts paper'
            }
    if str(symbol) == '0':
        pass
    else:
        return QUOTES[symbol.lower()[0]]

def get_rps_choice():
    choices = ['rock','paper','scissors']
    return random.choice(choices)

def get_rps_winner(a,b,quote=False):
    'return winner of rock paper scissors 1 = a, 2 = b, 0 = tie'
    rtn = 0
    winner = 0
    if a == b:                  # tie
        pass
    elif a.lower()[0] == 'r':   # rock
        if b.lower()[0] == 's':  # beats scissors
            rtn = 1
            winner = 'r'
        else:
            rtn = 2     # loses to paper
            winner = 'p'
    elif a.lower()[0] == 'p':   # paper
        if b.lower()[0] == 'r': # beats rock
            rtn = 1
            winner = 'p'
        else:
            rtn = 2             # loses to scissors
            winner = 's'
    elif a.lower()[0] == 's':   # scissors
        if b.lower()[0] == 'p': # beats paper
            rtn = 1
            winner = 's'
        else:
            rtn = 2             # loses to rock
            winner = 'r'
    else:
        raise IOError
    if not quote:
        return rtn
    else:
        return (rtn, generate_quote(winner))


