import pygame

screen = pygame.display.set_mode((400,800))
pygame.display.toggle_fullscreen()
running = True
tileSize = 90
clock = pygame.time.Clock()
mapHeight = 20
mapWidth = 40