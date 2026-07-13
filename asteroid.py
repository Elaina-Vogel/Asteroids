#asteroid class that inherits from CircleShape
import pygame
import circleshape
from constants import LINE_WIDTH

def __init__(self, x: float, y: float, radius: float) -> None:
    super().__init__(x, y, radius)

# PLayer class for game objects
class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        # overriding super
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt