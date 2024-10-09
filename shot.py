import pygame
from constants import SHOT_RADUIS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x: int, y :int) -> None:
        super().__init__(x, y, SHOT_RADUIS)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: int):
        self.position += self.velocity * dt
