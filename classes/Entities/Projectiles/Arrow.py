from classes.Entities.Projectile import Projectile

class Arrow(Projectile):
    def __init__(self, posX, posY, velX, velY):
        self.velX = velX
        self.velY = velY
        texture = "./media/arrow.png"
        super().__init__(speed=10, strength=5, texture=texture, posX=posX, posY=posY)
    def update(self):
        self.posX += self.velX
        self.posY += self.velY
        self.rect.topleft = (self.posX, self.posY)

        if self.posX - self.startX >= 800:
            self.dead = True
    
    def colideRect(self, rect):
        return self.rect.colliderect(rect)
