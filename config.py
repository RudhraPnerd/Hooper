class Screen:
    class States:
        STATE_GAME = 'game'
        STATE_GAME_OVER = 'game_over'
        STATE_HOME = 'home'


    SCREEN_SIZE = (600, 600)
    SCREEN_BG = (135, 206, 235)
    FPS = 60
    FONT = ("assets/ZenDots-Regular.ttf", 32)

class Files:
    class Sprites:
        BASKETBALL_SPRITE_FILE = 'assets/sprites/basketball.png'
        HOOP_SPRITE_FILE = 'assets/sprites/hoop.jpeg'

    class Buttons:
        REPLAY_FILE = 'assets/buttons/replay.png'
        HOME_FILE = 'assets/buttons/home.png'
        PLAY_FILE = 'assets/buttons/play.png'

    class Audio:
        CLICK_FILE = 'assets/audio/click.wav'
        SCORE_SOUND_EFFECT_FILE = 'assets/audio/score.wav'


    HIGH_SCORE_FILE = 'src/high_score.txt'