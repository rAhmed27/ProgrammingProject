import pygame 
import sys

res = width, height = 1600, 900
fps = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(res)
        self.clock = pygame.time.Clock()
    def update(self):
        pygame.display.flip()
        self.clock.tick(fps)
        pygame.display.set_caption(f'{self.clock.get_fps():.1f}')
    
    def newGame(self):
        pass

    def draw(self):
        self.screen.fill('black')

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

