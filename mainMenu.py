import pygame, sys

# Initialize Pygame
pygame.init()

# Window set-up
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Horror Game - Main Menu")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  
    pygame.display.flip()

pygame.quit()
sys.exit()
