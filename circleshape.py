import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding_with(self, obj: "CircleShape") -> bool:
        distance = self.position.distance_to(obj.position)
        radius_total = self.radius + obj.radius

        if distance <= radius_total:
            return True

        return False
