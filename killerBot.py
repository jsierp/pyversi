from copy import deepcopy
GSIZE = 8
SCORE_TABLE = [
    [5, 3, 1, 1, 1, 1, 3, 5],
    [3, 3, 1, 1, 1, 1, 3, 3],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 1, 1, 1, 1, 3, 3],
    [5, 3, 1, 1, 1, 1, 3, 5],
]


def returnMove(table, possibleMoves, me):
    bestMove = None
    bestPoints = -10000000
    for (x,y) in possibleMoves:
        copiedTable = deepcopy(table)
        move(copiedTable,x,y,me)
        points = evaluate(copiedTable,me)
        if points > bestPoints:
            bestPoints = points
            bestMove = (x,y)
    return bestMove

def evaluate(table,me):
    points = 0
    for x in range (GSIZE):
        for y in range (GSIZE):
            if table[x][y] == me:
                points = points + SCORE_TABLE[x][y]
    return points

def move(table,x,y,me):
    dirs=[(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
    for (dx, dy) in dirs:
        walkerX, walkerY = x+dx, y+dy
        while  0<= walkerX <GSIZE and 0<= walkerY <GSIZE and table[walkerX][walkerY] !=me:
            walkerX = walkerX+dx
            walkerY = walkerY+dy
        
        if 0<= walkerX <GSIZE and 0<= walkerY <GSIZE and table[walkerX][walkerY] == me:
            walkerX = walkerX - dx
            walkerY = walkerY - dy
            while walkerX != x and walkerY != y:
                table[walkerX][walkerY]=me
                walkerX = walkerX - dx
                walkerY = walkerY - dy

