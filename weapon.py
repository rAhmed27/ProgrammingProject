from spriteObjects import *

class Weapon(AnimatedSprites):
    def __init__(self, game, path='Textures/weapon/0.png', scale = 0.4, animTime = 90):
        super().__init__(game=game, path=path, scale=scale, animTime = animTime)
        self.images = deque([pygame.transform.smoothscale(img, (self.image.get_width()*scale, self.image.get_height()* scale)) for img in self.images])
        self.weaponPos = (halfWidth - self.images[0].get_width() // 2, height - self.images[0].get_height())
    
    def draw(self):
        self.game.screen.blit(self.images[0], self.weaponPos)
    
    def update(self):
        pass