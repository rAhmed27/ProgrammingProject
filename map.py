import pygame
import sys

res = width, height = 1600, 900
fps = 60

boundaryLine = 16 * [1]
innerLine = [1] + 14 * [False] + [1]

miniMap = [boundaryLine, innerLine, innerLine, innerLine, innerLine, innerLine, innerLine, innerLine, boundaryLine]

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
