import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Load character image (or replace with simple shape)
character = pygame.image.load("character.png")
x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # White background
    screen.blit(character, (x, 200))  # Draw character
    x += 2  # Move character

    if x > 600:
        x = -100  # Reset position

    pygame.display.update()
    clock.tick(30)  # 30 frames per second
