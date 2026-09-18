import time

import pygame
import sys
import assets as ast
import config as cfg
import ball
import hoop
import menus
import score_reading as sr
import coins_reading as cr
import skins as sk
import skin_reading as skr

pygame.init()

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)
pygame.display.set_caption('Hooper')

my_ball = ball.Ball(400, 400, 5)
my_hoop = hoop.Hoop(100, cfg.Screen.SCREEN_SIZE[1] - 50, 12, accel=1.5)

font_name, font_size = cfg.Screen.FONT
my_font = pygame.font.Font(font_name, font_size)

shop_font_name, shop_font_size = cfg.Screen.SHOP_FONT
shop_font = pygame.font.Font(shop_font_name, shop_font_size)

score = 0
high_score = sr.read_high_score()
coins = cr.read_coins()
skin = skr.read_skin()

previous_state = cfg.Screen.States.STATE_HOME
current_state = cfg.Screen.States.STATE_HOME

item_rects = []
buy_rects = []

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

                    elif ast.power_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        time.sleep(1)
                        running = False

            elif current_state == cfg.Screen.States.STATE_HOME:
                if event.button == 1:
                    if ast.play_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        score = 0
                        my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())
                        my_hoop.reset()
                        previous_state = cfg.Screen.States.STATE_HOME
                        current_state = cfg.Screen.States.STATE_GAME

                    elif ast.power_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        time.sleep(1)
                        running = False

            elif current_state == cfg.Screen.States.STATE_GAME:
                if event.button == 1:
                    if ast.shop_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        previous_state = cfg.Screen.States.STATE_GAME
                        current_state = cfg.Screen.States.STATE_SHOP

                    elif ast.power_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        running = False

            elif current_state == cfg.Screen.States.STATE_SHOP:
                if event.button == 1:
                    if ast.back_img_rect.collidepoint(event.pos):
                        ast.click.play()
                        previous_state = cfg.Screen.States.STATE_SHOP
                        current_state = cfg.Screen.States.STATE_GAME

                    else:
                        for i, rect in enumerate(item_rects):
                            if rect.collidepoint(event.pos):
                                item = menus.SHOP_ITEMS[i]
                                print(f"Viewing: {item['name']}")

                        for i, rect in enumerate(buy_rects):
                            if rect.collidepoint(event.pos):
                                item = menus.SHOP_ITEMS[i]
                                if coins >= item["cost"]:
                                    coins -= item["cost"]
                                    cr.save_coins(coins)
                                    if item["unlock"] == "realistic_hoop":
                                        sk.load_realistic_skin()
                                        skr.save_skin('realistic skin')
                                    ast.click.play()

                                else:
                                    current_state = cfg.Screen.States.STATE_BROKE

            elif current_state == cfg.Screen.States.STATE_BROKE:
                if event.button == 1:
                    if ast.back_img_rect.collidepoint(event.pos):
                        current_state = cfg.Screen.States.STATE_SHOP

    if current_state == cfg.Screen.States.STATE_GAME:
        if skin == 'realistic skin':
            sk.load_realistic_skin()


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
            ast.game_over.play()
            current_state = cfg.Screen.States.STATE_GAME_OVER

        ball_rect = ast.ball.get_rect(topleft=(my_ball.x, my_ball.y))
        hoop_rect = ast.hoop.get_rect(topleft=(my_hoop.x, my_hoop.y))

        if ball_rect.colliderect(hoop_rect):
            ast.score_sound_effect.play()
            score += 1
            coins += 1
            cr.save_coins(coins)
            my_ball.speed += 0.1
            my_ball.reset(cfg.Screen.SCREEN_SIZE[0], ast.ball.get_width())

            if score > high_score:
                high_score = score
                sr.save_high_score(high_score)

        ast.power_img_rect = ast.power.get_rect(topright=(500, 30))

        screen.fill(cfg.Screen.SCREEN_BG)

        score_text = my_font.render(f'Score: {score}', True, (0, 0, 0))
        high_score_text = my_font.render(f'High Score: {high_score}', True, (0, 0, 0))
        coins_text = my_font.render(f'Coins: {coins}', True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(high_score_text, (20, 60))
        screen.blit(coins_text, (20, 100))
        screen.blit(ast.ball, (my_ball.x, my_ball.y))
        screen.blit(ast.hoop, (my_hoop.x, my_hoop.y))
        screen.blit(ast.shop, ast.shop_img_rect)
        screen.blit(ast.power, ast.power_img_rect)

    elif current_state == cfg.Screen.States.STATE_GAME_OVER:
        menus.draw_game_over(screen, my_font)

    elif current_state == cfg.Screen.States.STATE_HOME:
        menus.draw_home(screen, my_font)

    elif current_state == cfg.Screen.States.STATE_SHOP:
        item_rects, buy_rects = menus.draw_shop(screen, shop_font, my_font)

    elif current_state == cfg.Screen.States.STATE_BROKE:
        menus.draw_broke(screen, my_font)

    pygame.display.flip()
    clock.tick(cfg.Screen.FPS)

pygame.quit()
sys.exit()