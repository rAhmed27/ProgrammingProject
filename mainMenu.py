import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Horror Game - Main Menu")
clock = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
darkRed = (150, 0, 0)

# Font
font = pygame.font.Font(None, 60)

# Define Button class
class Button:
    # Constructor class
    def __init__(self, text, position, size):
        self.text = text
        self.rect = pygame.Rect(position, size)
        self.color = red
        self.hoverColor = darkRed
        self.currentColor = self.color
    # Method to draw button rectangle
    def draw(self, surface):
        pygame.draw.rect(surface, self.currentColor, self.rect)
        text_surf = font.render(self.text, True, white)
        text_rect = text_surf.get_rect(center = self.rect.center)
        surface.blit(text_surf, text_rect)
    
    # Method to register mouse hovering over button
    def isHovered(self, mousePos):
        return self.rect.collidepoint(mousePos)
    
    # Method to update mouse colour if hovering over button
    def update(self, mousePos):
        self.currentColor = self.hoverColor if self.isHovered(mousePos) else self.color


# Create buttons
buttons = [
    Button("Start Game", (300, 200), (200, 60)),
    Button("Options", (300, 300), (200, 60)),
    Button("Quit", (300, 400), (200, 60))
]

# Main loop
running = True
while running:
    screen.fill(black)
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.isHovered(mousePos):
                    if button.text == "Quit":
                        running = False
                    elif button.text == "Start Game":
                        print("Start Game clicked!")
                        # TODO: Add game start logic
                    elif button.text == "Settings":
                        print("Options clicked!")
                        # TODO: Add options menu

    for button in buttons:
        button.update(mousePos)
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
