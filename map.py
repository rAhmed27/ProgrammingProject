import pygame
import sys
from settings import *

boundaryLine = 20 * [1]
innerlineW1 = [1] + 8 * [False] + 3 * [1] + 7 * [False] + [1]
innerlineW2 = [1] + 5 * [1] + 5 * [False]+ 8 * [False] + [1]
innerLineE = [1] + 18 * [False] + [1]

miniMap = [boundaryLine, innerlineW1, innerLineE, innerlineW2, innerlineW1, innerLineE, innerlineW2, innerLineE, boundaryLine]

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