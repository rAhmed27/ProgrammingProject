import pygame
import sys
from settings import *

miniMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, False, False, False, False, False, False, False, False, 1],
    [1, False, 1, 1, False, False, 1, 1, False, 1],
    [1, False, 1, False, False, False, False, 1, False, 1],
    [1, False, False, False, 1, 1, False, False, False, 1],
    [1, False, False, False, False, False, False, False, False, 1],
    [1, False, False, 1, 1, 1, False, False, False, 1],
    [1, False, False, False, False, False, False, False, False, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.miniMap = miniMap
        self.worldMap = {}
        self.rows = len(self.miniMap)
        self.columns = len(self.miniMap[0])
        self.getMap()

    def getMap(self):
        self.worldMap = {
            (i, j): value 
            for j, row in enumerate(self.miniMap)
            for i, value in enumerate(row)
            if value
        }
    def draw(self):
        for pos in self.worldMap:
            pygame.draw.rect(self.game.screen,'white',(pos[0] * 100, pos[1] * 100, 100, 100),2)