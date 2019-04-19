import random

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
DIRS = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
INF = 1000000
MAX_DEPTH = 5

def returnMove(table, possible_moves, me):
    best_move, best_val = None, -INF

    for x, y in possible_moves:
        changed = move(table, x, y, me)
        if not changed:
            raise Exception("Possible moves were wrong")

        val = alphabeta(table, MAX_DEPTH-1, me, -me, best_val)
        undo_move(table, changed, x, y)
        
        if val > best_val:
            best_move, best_val = (x, y), val
    
    return best_move

def undo_move(table, changed, x, y):
    for cx, cy in changed:
        table[cx][cy] *= -1
    table[x][y] = 0

def evaluate(table, me):
    return sum([SCORE_TABLE[x][y] for x in range(GSIZE) for y in range(GSIZE) if table[x][y]==me])

def alphabeta(table, depth, me, player, previous_best):
    best_val = -me*player*INF
    
    if depth == 0:
        return evaluate(table, me)

    for x in range(GSIZE):
        for y in range(GSIZE):
            changed = move(table, x, y, player)
            if changed:
                val = alphabeta(table, depth-1, me, -player, best_val)
                undo_move(table, changed, x, y)

                if me == player:
                    if val > previous_best:
                        return val
                    elif val > best_val:
                        best_val = val
                elif me != player:
                    if val < previous_best:
                        return val
                    elif val < best_val:
                        best_val = val
    
    if best_val == -me*player*INF:
        return alphabeta(table, depth-1, me, -player, best_val)
    
    return best_val

def move(table, x, y, player):
    changed = []
    if table[x][y] != 0:
        return []
    
    for (dx, dy) in DIRS:
        wx, wy = x+dx, y+dy
        while 0<=wx<GSIZE and 0<=wy<GSIZE and table[wx][wy] == -player:
            wx += dx
            wy += dy
        
        if 0<=wx<GSIZE and 0<=wy<GSIZE and table[wx][wy] == player:
            wx -= dx
            wy -= dy
            while wx != x or wy != y:
                table[wx][wy]=player
                changed.append((wx, wy))
                wx -= dx
                wy -= dy
    if len(changed) > 0:
        table[x][y] = player
    
    return changed
