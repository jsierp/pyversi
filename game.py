import pygame
import math
from pygame import gfxdraw
import importlib
import sys
from copy import deepcopy
from time import time

NUMBER_OF_GAMES = int(sys.argv[3])
firstName = sys.argv[1]
secondName = sys.argv[2]
firstPlayer = importlib.import_module(firstName)
secondPlayer = importlib.import_module(secondName)
firstTime = 0
secondTime = 0

GRAPHICS = firstName == 'human' or secondName == 'human' or len(sys.argv) > 4
maxTime = 0.01 if not GRAPHICS else 10000

GSIZE = 8
BLACK = 1
WHITE = -1
firstwins = 0
secondwins = 0
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
    if firstName == 'human':
        firstPlayer.init(pygame, cellSize)
    if secondName == 'human':
        secondPlayer.init(pygame, cellSize)

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

def ban(name):
    print("\nPermban gracza %s\n" % name)
    exit()

for i in range(NUMBER_OF_GAMES):
    initState()
    firstPlayerI = (i%2)*2-1
    player = BLACK

    if GRAPHICS:
        init()
        paint()
        sideBar()
    while True:
        checkAllPossibleMoves()
        if len(possibleMoves):
            start = time()
            if player == firstPlayerI:
                x, y = firstPlayer.returnMove(deepcopy(table), list(possibleMoves.keys()), player)
                turnTime = time()-start
                if turnTime > maxTime:
                    ban(firstName)
                else:
                    firstTime += turnTime
            else:
                x, y = secondPlayer.returnMove(deepcopy(table), list(possibleMoves.keys()), player)
                turnTime = time()-start
                if turnTime > maxTime:
                    ban(secondName)
                else:
                    secondTime += turnTime

            if move(x, y):
                countPoints()
                player *= -1
            else:
                name = firstName if player == firstPlayerI else secondName
        else:
            player *= -1
            checkAllPossibleMoves()
            if len(possibleMoves) == 0:
                if whitePoints > blackPoints:
                    firstwins += firstPlayerI == WHITE
                    secondwins += firstPlayerI == BLACK
                elif blackPoints > whitePoints:
                    firstwins += firstPlayerI == BLACK
                    secondwins += firstPlayerI == WHITE
                break
        if GRAPHICS:
            pygame.time.delay(int(sys.argv[4]))
            paint()
            sideBar()
    e = "\r" if i!=NUMBER_OF_GAMES-1 else "\n"
    print("Playing game %d, %s won %d with avg turn time: %.2e, %s won: %d with avg turn time: %.2e" % (
        i+1, firstName, firstwins, firstTime/(i+1)/30, secondName, secondwins, secondTime/(i+1)/30), end=e)
