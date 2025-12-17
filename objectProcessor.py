from spriteObjects import *
from enemyNPC import *

class ObjectProcessor:
    def __init__(self, game):
        self.game = game
        self.spriteList = []
        self.enemyList = []
        self.spritePathS = 'Textures/staticSprites/'
        self.spritePathA = 'Textures/dynamicSprites/'
        self.enemyPath = 'Textures/enemyNPC/'
        addSprite = self.addSprite
        # addEnemy = self.addEnemy

        addSprite(Sprite(game))
        addSprite(AnimatedSprites(game))
    
    def update(self):
        [self.update() for sprite in self.spriteList]
        [self.update() for enemyNPC in self.enemyList]
        
    def addSprite(self, sprite):
        self.spriteList.append(sprite)

   # def addEnemy(self, sprite):
        # self.enemyList.append(sprite)
