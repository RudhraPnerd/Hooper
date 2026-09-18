import config as cfg

def read_coins():
    try:
        with open(cfg.Files.COINS_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_coins(coins):
    with open(cfg.Files.COINS_FILE, "w") as f:
        f.write(str(coins))