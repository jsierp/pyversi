def returnMove(table, possibleMoves, player):
    GSIZE = 8
    bestMove = possibleMoves[0]
    bestGain = 0
    for x, y in possibleMoves:
        gain = 0
        for dX in (-1, 0, 1):
            for dY in (-1, 0 ,1):
                currX = x + dX
                currY = y + dY
                row = 0
                while(currX >= 0 and currX < GSIZE and currY < GSIZE and currY >= 0 and table[currX][currY] == player * -1):
                    row = row + 1
                    currX += dX
                    currY += dY
                if(currX >= 0 and currX < GSIZE and currY < GSIZE and currY >= 0 and table[currX][currY] == player):
                    gain = gain + row
        if gain > bestGain:
            bestGain = gain
            bestMove = (x, y)
    return bestMove
