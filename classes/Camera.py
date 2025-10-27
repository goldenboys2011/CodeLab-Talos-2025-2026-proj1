from config.config import mapWidth, mapHeight

class Camera:
    def __init__(self, width, height):
        self.offset_x = 0
        self.offset_y = 0
        self.width = width
        self.height = height

    def follow(self, target):
        self.offset_x = max(0, min(target.posX - self.width / 2 + 25, mapWidth * 50 - self.width) - 500)
        self.offset_y = max(0, min(target.posY - self.height / 2 + 25, mapHeight * 50 - self.height))