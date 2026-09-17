import random

class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def fall(self):
        self.y += self.speed

    def reset(self, screen_width, ball_width=0):
        self.x = random.randint(0, screen_width - ball_width)
        self.y = 0