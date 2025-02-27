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
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if balloon_x < mouse_x < balloon_x + balloon_width and balloon_y < mouse_y < balloon_y + balloon_height:
                balloon_x = random.randint(0, SCREEN_WIDTH - balloon_width)
                balloon_y = random.randint(0, SCREEN_HEIGHT - balloon_height)
    screen.blit(balloon_img, (balloon_x, balloon_y))
    pygame.display.update()

pygame.quit()