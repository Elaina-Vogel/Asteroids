#asteroid class that inherits from CircleShape
import pygame
from logger import log_event
import random
import circleshape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

# PLayer class for game objects
class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        # overriding super
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #else it splits
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        
        vel_one = self.velocity.rotate(random_angle)
        vel_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = vel_one * 1.2
        a2.velocity = vel_two * 1.2