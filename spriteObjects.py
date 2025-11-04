import pygame
from settings import *


class Sprite:
    def __init__(self, game, path= ('Textures/archon-fire.png'), pos = (12, 5)):
        self.game = game
        self.player = game.player
        self.X, self.Y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.normDist = 0, 0, 0, 0, 1, 1
        self.spriteHalfWdith = 0
    
    def getSpriteProjected(self):
        proj = screenDist / self.normDist
        projWidth, projHeight = proj * self.imageRatio, proj
        image = pygame.transform.scale(self.image, (projWidth, projHeight))
        self.spriteHalfWdith = projWidth // 2
        pos = self.screen_x - self.spriteHalfWdith, halfHeight - (projHeight // 2)
        self.game.rayCasting.objectsRender.append((self.normDist, image, pos))

    def getSprite(self):
        dx = self.X - self.player.X
        dy = self.Y - self.player.Y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta = self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        
        deltaRays = delta / deltaAngle
        self.screen_x = (halfNumRays + deltaRays) * scale

        self.dist = math.hypot(dx, dy)
        self.normDist = self.dist * math.cos(delta)
        if self.imageHalfWidth < self.screen_x < (width + self.imageHalfWidth) and self.normDist > 0.5:
            self.getSpriteProjected()
    
    def update(self):
        self.getSprite()