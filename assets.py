import pygame
import config as cfg

pygame.init()

screen = pygame.display.set_mode(cfg.Screen.SCREEN_SIZE)

ball = pygame.image.load(cfg.Files.Sprites.BASKETBALL_SPRITE_FILE).convert_alpha()
ball_img_rect = ball.get_rect(center=(cfg.Screen.SCREEN_SIZE[0] // 2, cfg.Screen.SCREEN_SIZE[1] // 2))

hoop = pygame.image.load(cfg.Files.Sprites.HOOP_SPRITE_FILE).convert_alpha()
hoop = pygame.transform.scale(hoop, (40, 40))

replay = pygame.image.load(cfg.Files.Buttons.REPLAY_FILE).convert_alpha()
replay = pygame.transform.scale(replay, (70, 70))
replay_img_rect = replay.get_rect(center=(200, 300))

home = pygame.image.load(cfg.Files.Buttons.HOME_FILE).convert_alpha()
home = pygame.transform.scale(home, (70, 70))
home_img_rect = home.get_rect(center=(400, 300))

play = pygame.image.load(cfg.Files.Buttons.PLAY_FILE).convert_alpha()
play = pygame.transform.scale(play, (70, 70))
play_img_rect = play.get_rect(center=(200, 300))

click = pygame.mixer.Sound(cfg.Files.Audio.CLICK_FILE)
score_sound_effect = pygame.mixer.Sound(cfg.Files.Audio.SCORE_SOUND_EFFECT_FILE)