import pygame

size = 600
screen = pygame.display.set_mode((size, size))

background_colour = (255,255,255)
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
