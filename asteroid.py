import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
            self.position += self.velocity * dt

    def split(self):
         self.kill()
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         log_event("asteroid_split")
         angle = random.uniform(20, 50)
         new_radius = self.radius - ASTEROID_MIN_RADIUS
         asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
         asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
         asteroid1.velocity = self.velocity.rotate(angle) * 1.2
         asteroid2.velocity = self.velocity.rotate(-angle) * 1.2


