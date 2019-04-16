import math
import pygame
from pygame import gfxdraw

GSIZE = 8
BLACK = 1
WHITE = -1

size = 600
p1 = 0
p2 = 0
cellSize = size / GSIZE
rad = cellSize * 0.4
strokeWidth = 5
sideBarSize = 400
player = 1;

screen = pygame.display.set_mode((size + sideBarSize, size))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', int(sideBarSize*0.14))

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
    pygame.draw.rect(screen, (0, 255, 0), (size, 0, sideBarSize, size));
    textsurface = myfont.render('current:', False, (0, 0, 0))
    screen.blit(textsurface,(size, 10))
    if(player == 1): paintCell(15, 0, (255, 255, 255))
    else: paintCell(10, 0, (0, 0, 0))
    pygame.display.flip()

def init():
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, size, size));
    for i in range(GSIZE):
        for j in range(GSIZE):
            pygame.draw.rect(screen, (0, 0, 0), (i * cellSize, j * cellSize, cellSize, cellSize), strokeWidth)
    pygame.display.flip()

def paint():
    for i in range(GSIZE):
        for j in range(GSIZE):
            if(table[i][j] == 1):
                paintCell(i, j, (0, 0, 0))
            elif(table[i][j] == -1):
                paintCell(i, j, (255, 255, 255))

    pygame.display.flip()

def move(x, y):
    global player
    if(table[x][y] == 0):
        table[x][y] = player
        player *= -1;


init()
paint();
move(2, 2);
paint();
sideBar();

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = math.floor(x / cellSize)
            y = math.floor(y / cellSize)

            print(str(x)+" "+str(y));
