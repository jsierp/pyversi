import pygame
import math
from pygame import gfxdraw
import human, stupidBot

NUMBER_OF_GAMES = 1000
blackFunction = stupidBot.returnMove
whiteFunction = stupidBot.returnMove

GRAPHICS = False

GSIZE = 8
BLACK = 1
WHITE = -1
bwins = 0
wwins = 0
size = 600
cellSize = size / GSIZE
rad = cellSize * 0.4
strokeWidth = 5
sideBarSize = 400
possibleMoves = dict()
player = 1

if GRAPHICS:
    screen = pygame.display.set_mode((size + sideBarSize, size))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', int(sideBarSize*0.14))

    human.init(pygame, cellSize)

def initState():
    global whitePoints, blackPoints, table
    whitePoints = 0
    blackPoints = 0
    player = 1

    table = [[0 for _ in range(GSIZE)] for _ in range(GSIZE)]
    table[int(GSIZE/2)][int(GSIZE/2)] = 1
    table[int(GSIZE/2 - 1)][int(GSIZE/2 - 1)] = 1
    table[int(GSIZE/2 - 1)][int(GSIZE/2)] = -1
    table[int(GSIZE/2)][int(GSIZE/2 - 1)] = -1

def paintCell(x, y, color):
    pygame.gfxdraw.filled_circle(screen, int((x + 0.5) * cellSize), int((y + 0.5) * cellSize), int(rad), (0, 0, 0))
    pygame.gfxdraw.filled_circle(screen, int((x + 0.5) * cellSize), int((y + 0.5) * cellSize), int(rad - strokeWidth), color)
    pygame.gfxdraw.aacircle(screen, int((x + 0.5) * cellSize), int((y + 0.5) * cellSize), int(rad), (0, 0, 0))
    pygame.gfxdraw.aacircle(screen, int((x + 0.5) * cellSize), int((y + 0.5) * cellSize), int(rad - strokeWidth), color)


def sideBar():
    global player
    countPoints()
    pygame.draw.rect(screen, (0, 255, 0), (size, 0, sideBarSize, size));

    paintCell(9,2, (255,255,255))
    whitesurface = myfont.render(str(whitePoints), True, (0, 0, 0))
    screen.blit(whitesurface,(size + 95, cellSize*3))

    paintCell(9,4, (0,0,0))
    blacksurface = myfont.render(str(blackPoints), True, (0, 0, 0))
    screen.blit(blacksurface,(size + 95, cellSize*5))

    if player == WHITE:
        paintCell(10, 0, (255, 255, 255))
    else:
        paintCell(10, 0, (0, 0, 0))
    pygame.display.flip()


def init():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, size, size));
    for i in range(GSIZE):
        for j in range(GSIZE):
            pygame.draw.rect(screen, (0, 0, 0), (i * cellSize, j * cellSize, cellSize, cellSize), strokeWidth)
    pygame.display.flip()

def countPoints():
    global whitePoints, blackPoints

    whitePoints, blackPoints = 0, 0
    for i in range (GSIZE):
        for j in range (GSIZE):
            if table[i][j]==BLACK:
                blackPoints=blackPoints+1
            elif table[i][j]==WHITE:
                whitePoints=whitePoints+1

def paint():
    for i in range(GSIZE):
        for j in range(GSIZE):
            if(table[i][j] == 1):
                paintCell(i, j, (0, 0, 0))
            elif(table[i][j] == -1):
                paintCell(i, j, (255, 255, 255))

    pygame.display.flip()

def end():
    global whitePoints, blackPoints, bwins, wwins
    if whitePoints > blackPoints:
        bwins += 1
    elif blackPoints > whitePoints:
        wwins += 1

def move(x, y):
    global possibleMoves
    global player
    if((x,y) in possibleMoves):
        for cX, cY in possibleMoves[(x, y)]:
            table[cX][cY] = player
        table[x][y] = player
        return True
    return False

def checkAllPossibleMoves():
    global player, possibleMoves
    possibleMoves = dict()
    for x in range(GSIZE):
        for y in range(GSIZE):

            if(table[x][y] == 0):
                changed = []
                for dX in (-1, 0, 1):
                    for dY in (-1, 0 ,1):
                        currX = x + dX
                        currY = y + dY
                        row = []
                        while(currX >= 0 and currX < GSIZE and currY < GSIZE and currY >= 0 and table[currX][currY] == player * -1):
                            row.append((currX, currY))
                            currX += dX
                            currY += dY
                        if(currX >= 0 and currX < GSIZE and currY < GSIZE and currY >= 0 and table[currX][currY] == player):
                            changed = changed + row

                if(len(changed) > 0):
                    possibleMoves[(x, y)] = changed


for i in range(NUMBER_OF_GAMES):
    print("Playing game %d" % i, end="\r")
    initState()
    if GRAPHICS:
        init()
        paint()
        sideBar()
    while True:
        checkAllPossibleMoves()
        if len(possibleMoves):
            if player == WHITE:
                x, y = whiteFunction(table, list(possibleMoves.keys()), player)
            else:
                x, y = blackFunction(table, list(possibleMoves.keys()), player)

            if move(x, y):
                countPoints()
                player *= -1
            else:
                raise Exception("Nie wiem co zrobic %d" % player)
        else:
            player *= -1
            checkAllPossibleMoves()
            if len(possibleMoves) == 0:
                end()
                break
        if GRAPHICS:
            pygame.time.delay(100)
            paint()
            sideBar()
print("White won: %d games, black won %d games" % (wwins, bwins))
