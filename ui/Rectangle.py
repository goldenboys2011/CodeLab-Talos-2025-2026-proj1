import pygame
from config.config import screen
class Rectangle():
    def __init__(self,  color, width,  height, xPos, yPos, givePoints):
        self.color = color
        self.x = xPos
        self.y = yPos
        self.w = width
        self.h = height
        self.text = False
        if givePoints == 1:
            self.points = 20
        else:
            self.points = 0
        
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface.fill(color)
        
        self.rect = self.surface.get_rect(topleft=(xPos, yPos))
        
    def updatePosition(self, newX, newY):
        self.rect.topleft = (newX, newY)
        self.x = newX
        self.y = newY

    def updateText(self, newText, fsize, text_color):
        self.text = newText
        font = pygame.font.Font(None, fsize)
        self.surface.fill((0, 0, 0, 0))  # Transparent fill
        text_surface = font.render(newText, True, text_color)
        text_rect = text_surface.get_rect(center=(self.w // 2, self.h // 2))
        self.surface.blit(text_surface, text_rect)

    def clearText(self):
        self.text = ""
        self.surface.fill((0, 0, 0, 0))  # Transparent fill

    def drawBlock(self):
        screen.blit(self.surface, self.rect)
            
    def colideRect(self, rect):
        return self.rect.colliderect(rect)