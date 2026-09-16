import config as cfg

def read_high_score():
    try:
        with open(cfg.Files.HIGH_SCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(new_score):
    with open(cfg.Files.HIGH_SCORE_FILE, "w") as f:
        f.write(str(new_score))