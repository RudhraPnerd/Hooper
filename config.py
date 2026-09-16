class Screen:
    class States:
        STATE_GAME = 'game'
        STATE_GAME_OVER = 'game_over'


    SCREEN_SIZE = (800, 600)
    SCREEN_BG = (135, 206, 235)
    FPS = 60
    FONT = ("assets/ZenDots-Regular.ttf", 32)

class Files:
    class Sprites:
        BASKETBALL_SPRITE_FILE = 'assets/sprites/basketball.png'
        HOOP_SPRITE_FILE = 'assets/sprites/hoop.jpeg'

    class Buttons:
        CHECK_CIRCLE_FILE = 'assets/buttons/check_circle.png'


    HIGH_SCORE_FILE = 'src/high_score.txt'