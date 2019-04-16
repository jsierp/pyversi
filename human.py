import math

pygame = None
cellSize = None

def init(pg, cs):
    global pygame, cellSize
    pygame = pg
    cellSize = cs

def returnMove(table, possibleMoves, player):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = math.floor(x / cellSize)
                y = math.floor(y / cellSize)
                if (x, y) in possibleMoves:
                    return x, y
                    