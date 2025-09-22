import pygame
import math
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.X, self.Y = playerPOS
        self.angle = playerAngle
    
    def pos(self):
        return self.X, self.Y
    
    def mapPos(self):
        return int(self.X), int(self.Y)
    
    def movement(self):
        sinA = math.sin(self.angle)
        cosA = math.cos(self.angle)
        dx, dy = 0, 0
        speed = playerSpeed * self.game.deltaTime
        speedSin = speed * sinA
        speedCos = speed * cosA
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx = dx + speedCos
            dy = dy + speedSin
        if keys[pygame.K_a]:
            dx = dx + speedSin
            dy = dy - speedCos
        if keys[pygame.K_s]:
            dx = dx - speedCos
            dy = dy - speedSin
        if keys[pygame.K_d]:
            dx = dx - speedSin
            dy = dy + speedCos 
        self.checkWallCollision(dx,dy)
        # if keys[pygame.K_LEFT]:
            # self.angle = self.angle - playerROTspeed * self.game.deltaTime
        # if keys[pygame.K_RIGHT]:
            # self.angle = self.angle + playerROTspeed * self.game.deltaTime 
        self.angle = self.angle % math.tau

    def checkWall(self, x, y):
        if (x,y) not in self.game.map.worldMap:
            return (x,y)
    def checkWallCollision(self, dx, dy):
        scale = playerScaleSize / self.game.deltaTime

        if self.checkWall(int(self.X + dx * scale), int(self.Y)):
            self.X = self.X + dx
        if self.checkWall(int(self.X), int(self.Y + dy * scale)):
            self.Y = self.Y + dy   

    def draw(self):
        pygame.draw.line(self.game.screen, 'blue', (self.X * 100, self.Y * 100), (self.X * 100 + width * math.cos(self.angle), self.Y * 100 + width * math.sin(self.angle)), 2) 
        pygame.draw.circle(self.game.screen, 'red', (self.X * 100, self.Y * 100), 15)
    
    def controlMouse(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX < mouseLeftBorder or mouseX > mouseRightBorder:
            pygame.mouse.set_pos([halfWidth, halfHeight])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max( -mouseMaxRel, min(mouseMaxRel, self.rel))
        self.angle = self.angle + self.rel * mouseSensitivity * self.game.deltaTime


    def update(self):
        self.movement()
        self.controlMouse()