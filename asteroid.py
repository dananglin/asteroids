import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: int):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        random_angle = random.uniform(20, 50)
        vec_0 = self.velocity.rotate(random_angle)
        vec_1 = self.velocity.rotate(-random_angle)

        new_asteroid_0 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_0.velocity = vec_0 * 1.2

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vec_1 * 1.2
