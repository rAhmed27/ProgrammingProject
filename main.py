import pygame 
import sys
from settings import *
from map import *
from player import *
from rayCasting import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(res)
        self.clock = pygame.time.Clock()
        self.deltaTime = 1
        self.newGame()
    def update(self):
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.deltaTime = self.clock.tick(fps)
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}')
    def newGame(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)
    def draw(self):
        self.screen.fill('black')
        # self.map.draw()
        self.player.draw()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_DOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.checkEvents()
            self.update()
            self.draw()
        
if __name__ == '__main__':
    game = Game()
    game.run()

