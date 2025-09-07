import pygame
import sys

res = width, height = 1600, 900
fps = 60

boundaryLine = 16 * [1]
innerLine = [1] + 14 * [False] + [1]

miniMap = [boundaryLine, innerLine, innerLine, innerLine, innerLine, innerLine, innerLine, innerLine, boundaryLine]
print(miniMap)
class Map:
    def __init__(self, game):
        self.game = game
        self.miniMap = miniMap
        self.worldMap = {}
        self.rows = len(self.miniMap)
        self.columns = len(self.miniMap[0])
        self.getMap()