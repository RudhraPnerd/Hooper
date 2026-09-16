class Hoop:
    def __init__(self, x, y, max_speed, accel=0.8, friction=0.85):
        self.x = x
        self.y = y
        self.vel = 0
        self.max_speed = max_speed
        self.accel = accel
        self.friction = friction

    def move_left(self):
        self.vel -= self.accel
        if self.vel < -self.max_speed:
            self.vel = -self.max_speed

    def move_right(self):
        self.vel += self.accel
        if self.vel > self.max_speed:
            self.vel = self.max_speed

    def update(self):
        self.vel *= self.friction
        if abs(self.vel) < 0.1:
            self.vel = 0
        self.x += self.vel