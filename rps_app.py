import random

def get_rps_choice():
    choices = ['rock','paper','scissors']
    return random.choice(choices)

def get_rps_winner(a,b):
    'return winner of rock paper scissors 1 = a, 2 = b, 0 = tie'
    rtn = 0
    if a == b:                  # tie
        pass
    elif a.lower()[0] == 'r':   # rock
        if b.lower()[0] == 's':  # beats scissors
            rtn = 1
        else:
            rtn = 2             # loses to paper
    elif a.lower()[0] == 'p':   # paper
        if b.lower()[0] == 'r': # beats rock
            rtn = 1
        else:
            rtn = 2             # loses to scissors
    elif a.lower()[0] == 's':   # scissors
        if b.lower()[0] == 'p': # beats paper
            rtn = 1
        else:
            rtn = 2             # loses to rock
    else:
        raise IOError
    return rtn


