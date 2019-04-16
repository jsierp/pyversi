import random

def returnMove(table, possibleMoves, player):

    r = random.randint(0, len(possibleMoves) - 1)
    return possibleMoves[r]
