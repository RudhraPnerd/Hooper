import pygame
import config as cfg

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)

ball = pygame.image.load(cfg.Files.Sprites.BASKETBALL_SPRITE_FILE).convert_alpha()
ball_img_rect = ball.get_rect(center=(400, 300))

hoop = pygame.image.load(cfg.Files.Sprites.HOOP_SPRITE_FILE).convert_alpha()
hoop = pygame.transform.scale(hoop, (40, 40))