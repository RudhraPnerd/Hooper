class Screen:
    class States:
        STATE_GAME = 'game'
        STATE_GAME_OVER = 'game_over'
        STATE_HOME = 'home'
        STATE_SHOP = 'shop'


    SCREEN_SIZE = (600, 600)
    SCREEN_BG = (135, 206, 235)
    FPS = 60
    FONT = ("assets/ZenDots-Regular.ttf", 32)
    SHOP_FONT = ('assets/ZenDots-Regular.ttf', 16)

class Files:
    class Sprites:
        class HoopSkins:
            REALISTIC_FILE = 'assets/sprites/hoop-skins/realistic.jpg'
        BASKETBALL_SPRITE_FILE = 'assets/sprites/basketball.png'
        HOOP_SPRITE_FILE = 'assets/sprites/hoop.jpeg'

    class Buttons:
        REPLAY_FILE = 'assets/buttons/replay.png'
        HOME_FILE = 'assets/buttons/home.png'
        PLAY_FILE = 'assets/buttons/play.png'
        POWER_FILE = 'assets/buttons/power.png'
        SHOP_FILE = 'assets/buttons/shop.png'
        BACK_FILE = 'assets/buttons/back.png'

    class Audio:
        CLICK_FILE = 'assets/audio/click.wav'
        SCORE_SOUND_EFFECT_FILE = 'assets/audio/score.wav'
        GAME_OVER_FILE = 'assets/audio/game_over.wav'
        BROKE_SOUND_EFFECT_FILE = 'assets/audio/broke.wav'


    HIGH_SCORE_FILE = 'src/high_score.txt'
    COINS_FILE = 'src/coins.txt'