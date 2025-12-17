import pygame
from settings import *
import os
from collections import deque

class Sprite:
    def __init__(self, game, path= ('Textures/enemyNPC/archon-fire.png'), pos = (4.5, 5.5), scale = 1.07, shift = - 0.1):
        self.game = game
        self.player = game.player
        self.X, self.Y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.imageWidth = self.image.get_width()
        self.imageHalfWidth = self.image.get_width() // 2
        self.imageRatio = self.imageWidth / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.normDist = 0, 0, 0, 0, 1, 1
        self.spriteHalfWidth = 0
        self.spriteScale = scale
        self.spriteHeightShift = shift
    
    def getSpriteProjected(self):
        proj = screenDist / self.normDist * self.spriteScale
        projWidth, projHeight = proj * self.imageRatio, proj
        image = pygame.transform.scale(self.image, (projWidth, projHeight))
        self.spriteHalfWidth = projWidth // 2
        heightShift = projHeight * self.spriteHeightShift
        pos = self.screen_x - self.spriteHalfWidth, halfHeight - (projHeight // 2 + heightShift)
        self.game.rayCasting.objectsRender.append((self.normDist, image, pos))

    def getSprite(self):
        dx = self.X - self.player.X
        dy = self.Y - self.player.Y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)
#
        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        
        deltaRays = delta / deltaAngle
        self.screen_x = (halfNumRays + deltaRays) * scale

        self.dist = math.hypot(dx, dy)
        self.normDist = self.dist * math.cos(delta)
        if -self.imageHalfWidth < self.screen_x < (width + self.imageHalfWidth) and self.normDist > 0.5:
            self.getSpriteProjected()
    
    def update(self):
        self.getSprite()

class AnimatedSprites(Sprite):
    def __init__(self, game, path = 'Textures/enemyNPC/archon-fire.png', pos = (7.5, 4.5), scale = 1.5, shift = -0.1, animTime = 120):
        super().__init__(game, path, pos, scale, shift)
        self.animTime = animTime
        self.path = path.rsplit('/', 1)[0]
        self.images = self.getImages(self.path)
        self.animTimePrev = pygame.time.get_ticks()
        self.animTrigger = False

    def update(self):
        super().update()
        self.checkAnimTime()
        self.animate(self.images)
    
    def animate(self, images):
        if self.animTrigger:
            images.rotate(-1)
            self.image = images[0]
    
    def checkAnimTime(self):
        self.animTrigger = False
        timeNow = pygame.time.get_ticks()
        if timeNow - self.animTimePrev > self.animTime:
            self.animTimePrev = timeNow
            self.animTrigger = True
    
    def getImages(self, path):
        images= deque()
        for fileName in os.listdir(path):
            if os.path.isfile(os.path.join(path, fileName)):
                img = pygame.image.load(path + '/' + fileName).convert_alpha()
                images.append(img)
        return images



