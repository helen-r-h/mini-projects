import pygame
import sys

pygame.init() #inits the modules??
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # draw elements
    pygame.display.update()
    clock.tick(60)
