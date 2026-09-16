import pygame
import sys
import assets as ast
import config as cfg
import ball

pygame.init()

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)
pygame.display.set_caption('Hooper')

my_ball = ball.Ball(400, 400, 5)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    my_ball.fall()

    if my_ball.y > cfg.Screen.SCREEN_SIZE[1]:
        my_ball.reset(cfg.Screen.SCREEN_SIZE[0])

    screen.fill(cfg.Screen.SCREEN_BG)

    screen.blit(ast.ball, (my_ball.x, my_ball.y))

    pygame.display.flip()
    clock.tick(cfg.Screen.FPS)

pygame.quit()
sys.exit()