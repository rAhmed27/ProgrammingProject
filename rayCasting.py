import pygame
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game
        self.rayCastResult = []
        self.objectsRender = []
        self.textures = self.game.renderObject. wallTextures
    
    def rayCast(self):
        playerX, playerY = self.game.player.pos()
        mapX, mapY = self.game.player.mapPos()
        vertTexture, horTexture = 1, 1
        rayAngle = self.game.player.angle - (halfFOV + 0.0001)
        for ray in range(int(numRays)):
            sinRC = math.sin(rayAngle)
            cosRC = math.cos(rayAngle)
            rayAngle = rayAngle + deltaAngle

            if sinRC > 0:
                horY, dy = mapY + 1, 1
            else:
                horY, dy = mapY - 0.000001, -1
            horDepth = (horY - playerY) / sinRC
            horX = cosRC * horDepth + playerX
            deltaDepth = dy / sinRC
            dx = deltaDepth * cosRC

            for i in range(maxDepth):
                horTile = int(horX), int(horY)
                if horTile in self.game.map.worldMap:
                    horTexture = self.game.map.worldMap[horTile]
                    break
                horX = horX + dx
                horY = horY + dy
                horDepth = horDepth + deltaDepth

            if cosRC > 0:
                vertX, dx = mapX + 1, 1
            else:
                vertX, dx = mapX - 0.000001, -1
            vertDepth = (vertX - playerX)/cosRC
            vertY = sinRC * vertDepth + playerY
            deltaDepth = dx /cosRC
            dy = deltaDepth * sinRC

            for i in range(maxDepth):
                vertTile = int(vertX), int(vertY)
                if vertTile in self.game.map.worldMap:
                    vertTexture = self.game.map.worldMap[vertTile]
                    break
                vertX = vertX + dx
                vertY = vertY + dy
                vertDepth = vertDepth + deltaDepth

            if vertDepth < horDepth:
                depth = vertDepth
            else:
                depth = horDepth
        
            depth *= math.cos(self.game.player.angle - rayAngle)
            depth = max(depth, 0.0001)
            projHeight = screenDist / depth
            colour = [255 / (1 + depth ** 5 * 0.00002)] * 3
            pygame.draw.rect(self.game.screen, colour, (ray * scale, halfHeight - projHeight // 2, scale, projHeight))

            # pygame.draw.line(self.game.screen, 'green', (100 * playerX, 100 * playerY), (100 * playerX + 100 * cosRC * depth, 100 * playerY + 100 * sinRC * depth), 2)
            rayAngle = rayAngle + deltaAngle
    def update(self):
        self.rayCast()