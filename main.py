import pygame
import sys
import assets as ast
import config as cfg
import ball
import hoop
import score_reading as sr

pygame.init()

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)
pygame.display.set_caption('Hooper')

my_ball = ball.Ball(400, 400, 5)
my_hoop = hoop.Hoop(100, 550, 5)

font_name, font_size = cfg.Screen.FONT
my_font = pygame.font.Font(font_name, font_size)

score = 0
high_score = sr.read_high_score()

current_state = cfg.Screen.States.STATE_GAME
previous_state = cfg.Screen.States.STATE_GAME

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        my_hoop.move_right()
    if keys[pygame.K_LEFT]:
        my_hoop.move_left()

    my_hoop.update()

    if my_hoop.x < 0:
        my_hoop.x = 0
        my_hoop.vel = 0

    elif my_hoop.x + ast.hoop.get_width() > cfg.Screen.SCREEN_SIZE[0]:
        my_hoop.x = cfg.Screen.SCREEN_SIZE[0] - ast.hoop.get_width()
        my_hoop.vel = 0

    my_ball.fall()

    if my_ball.y > cfg.Screen.SCREEN_SIZE[1]:
        my_ball.reset(cfg.Screen.SCREEN_SIZE[0])

    ball_rect = ast.ball.get_rect(topleft=(my_ball.x, my_ball.y))
    hoop_rect = ast.hoop.get_rect(topleft=(my_hoop.x, my_hoop.y))

    if ball_rect.colliderect(hoop_rect):
        score += 1
        my_ball.reset(cfg.Screen.SCREEN_SIZE[0])

        if score > high_score:
            high_score = score
            sr.save_high_score(high_score)



    score_text = my_font.render(f'Score: {score}', True, (0, 0, 0))
    high_score_text = my_font.render(f'High Score: {high_score}', True, (0, 0, 0))

    screen.fill(cfg.Screen.SCREEN_BG)

    screen.blit(score_text, (20, 20))
    screen.blit(high_score_text, (20, 60))
    screen.blit(ast.ball, (my_ball.x, my_ball.y))
    screen.blit(ast.hoop, (my_hoop.x, my_hoop.y))

    pygame.display.flip()
    clock.tick(cfg.Screen.FPS)

pygame.quit()
sys.exit()