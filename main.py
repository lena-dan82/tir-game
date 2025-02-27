import pygame
import random


pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)


balloon_img = pygame.image.load("img/balloon.png")
balloon_width = 80
balloon_height = 80
balloon_x = random.randint(0, SCREEN_WIDTH - balloon_width)
balloon_y = random.randint(0, SCREEN_HEIGHT - balloon_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
        pass

pygame.quit()