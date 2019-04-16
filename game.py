import pygame
from pygame import gfxdraw

GSIZE = 8
size = 600
cellSize = size / GSIZE
rad = cellSize * 0.4
strokeWidth = 5
screen = pygame.display.set_mode((size, size))

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
                pygame.gfxdraw.filled_circle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad), (0, 0, 0))
                pygame.gfxdraw.aacircle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad), (0, 0, 0))
            elif(table[i][j] == -1):
                pygame.gfxdraw.filled_circle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad), (0, 0, 0))
                pygame.gfxdraw.filled_circle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad - strokeWidth), (255, 255, 255))
                pygame.gfxdraw.aacircle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad), (0, 0, 0))
                pygame.gfxdraw.aacircle(screen, int((i + 0.5) * cellSize), int((j + 0.5) * cellSize), int(rad - strokeWidth), (255, 255, 255))

    pygame.display.flip()

table = [[0 for _ in range(GSIZE)] for _ in range(GSIZE)]

init()
paint();


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
