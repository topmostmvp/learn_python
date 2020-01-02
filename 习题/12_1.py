import sys
import pygame

def blue():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (0, 0, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYUP:
                print(event.type)
        screen.fill(bg_color)
        pygame.display.flip()
blue()   