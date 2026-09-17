import pygame
import sys
import assets as ast
import config as cfg
import ball
import hoop
import menus
import score_reading as sr

pygame.init()

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)
pygame.display.set_caption('Hooper')

my_ball = ball.Ball(400, 400, 5)
my_hoop = hoop.Hoop(100, cfg.Screen.SCREEN_SIZE[1] - 50, 12, accel=1.5)

font_name, font_size = cfg.Screen.FONT
my_font = pygame.font.Font(font_name, font_size)

score = 0
high_score = sr.read_high_score()

previous_state = cfg.Screen.States.STATE_HOME
current_state = cfg.Screen.States.STATE_HOME

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if current_state == cfg.Screen.States.STATE_GAME_OVER:
                if event.key == pygame.K_r:
                    score = 0
                    my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())
                    my_hoop.reset()
                    current_state = cfg.Screen.States.STATE_GAME

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == cfg.Screen.States.STATE_GAME_OVER:
                if event.button == 1:
                    if ast.replay_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        score = 0
                        my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())
                        my_hoop.reset()
                        previous_state = cfg.Screen.States.STATE_GAME_OVER
                        current_state = cfg.Screen.States.STATE_GAME

                    elif ast.home_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        score = 0
                        my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())
                        my_hoop.reset()
                        previous_state = cfg.Screen.States.STATE_GAME_OVER
                        current_state = cfg.Screen.States.STATE_HOME

            elif current_state == cfg.Screen.States.STATE_HOME:
                if event.button == 1:
                    if ast.play_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        score = 0
                        my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())
                        my_hoop.reset()
                        previous_state = cfg.Screen.States.STATE_HOME
                        current_state = cfg.Screen.States.STATE_GAME

    if current_state == cfg.Screen.States.STATE_GAME:
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
            current_state = cfg.Screen.States.STATE_GAME_OVER

        ball_rect = ast.ball.get_rect(topleft=(my_ball.x, my_ball.y))
        hoop_rect = ast.hoop.get_rect(topleft=(my_hoop.x, my_hoop.y))

        if ball_rect.colliderect(hoop_rect):
            ast.score_sound_effect.play()
            score += 1
            my_ball.speed += 0.1
            my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())

            if score > high_score:
                high_score = score
                sr.save_high_score(high_score)

        screen.fill(cfg.Screen.SCREEN_BG)

        score_text = my_font.render(f'Score: {score}', True, (0, 0, 0))
        high_score_text = my_font.render(f'High Score: {high_score}', True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(high_score_text, (20, 60))
        screen.blit(ast.ball, (my_ball.x, my_ball.y))
        screen.blit(ast.hoop, (my_hoop.x, my_hoop.y))

    elif current_state == cfg.Screen.States.STATE_GAME_OVER:
        menus.draw_game_over(screen, my_font)

    elif current_state == cfg.Screen.States.STATE_HOME:
        menus.draw_home(screen, my_font)

    pygame.display.flip()
    clock.tick(cfg.Screen.FPS)

pygame.quit()
sys.exit()