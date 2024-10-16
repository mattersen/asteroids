import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        new_ast_vector1 = self.velocity.rotate(split_angle)
        new_ast_vector2 = self.velocity.rotate(-split_angle)
        new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        ast1.velocity = new_ast_vector1 * 1.2
        ast2.velocity = new_ast_vector2 * 1.2
