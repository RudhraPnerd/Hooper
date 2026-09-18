import assets as ast
import config as cfg
import pygame

def load_realistic_skin():
    ast.hoop = pygame.image.load(cfg.Files.Sprites.HoopSkins.REALISTIC_FILE).convert_alpha()
    ast.hoop = pygame.transform.scale(ast.hoop, (40, 40))