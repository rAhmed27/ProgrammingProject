import pygame
from settings import *

class renderObject:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTexture()
        self.skyImage = self.getTexture('Textures/gloomy_up.png', (width, halfHeight))
        self.skyOffset = 0
    
    def draw(self):
        self.drawBackdrop()
        self.renderGameObjects()
    
    def drawBackdrop(self):
        self.skyOffset = (self.skyOffset + 4.5 * self.game.player.rel) % width
        self.screen.blit(self.skyImage, (-self.skyOffset, 0))
        self.screen.blit(self.skyImage, (-self.skyOffset + width, 0))
        pygame.draw.rect(self.screen, floorColour, (0, halfHeight, width, height))



    def renderGameObjects(self):
        listObjects = sorted(self.game.rayCasting.objectsRender, key=lambda t: t[0], reverse = True)
        for depth, image, pos in listObjects:
            self.screen.blit(image, pos)
    
    @staticmethod
    def getTexture(path, res = (textureSize, textureSize)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
        
    def loadWallTexture(self):
        return {
            1: self.getTexture('Textures/gameFloor.png')
        }