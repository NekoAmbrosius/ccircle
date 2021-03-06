class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.fx = 1
        self.fy = 17
        self.mass = 1
        self.rapeed = 0

    def apply_force(self, fx, fy):
        self.fx += fx
        self.fy += fy

    def draw(self, window):
        window.drawCircle(self.x, self.y, 16)

    def update(self, dt):
        self.x += self.vx
        self.y += dt * self.vy
        accel_y = self.fy / self.mass
        self.vx += self.vx
        self.vy += dt * accel_y
        self.fx = 17
        self. fy = 34

        if self.y > 500:
            self.vy *= -0.99
            self.y = 500