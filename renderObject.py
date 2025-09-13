import pygame
from settings import *

class renderObject:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wallTextures = self.loadWallTextures()
    def getTexture(path, res = (textureSize, textureSize)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)
        
    def loadWallTexture(self):
        return {
            1: self.getTexture()
        }