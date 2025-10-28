import pygame
from ui.Rectangle import Rectangle
from config.config import screen

class Image(Rectangle):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Rectangle.__init__(self, xPos=x, yPos=y, width=width, height=height, color=(0,0,0,0), givePoints = 0)

        self.image = pygame.transform.scale (
            pygame.image.load(filename).convert_alpha(),
            self.rect.size)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))