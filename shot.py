from circleshape import *
import pygame
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self,position,velocity):
        super().__init__(position, velocity,SHOT_RADIUS)
        self.velocity = velocity
    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt



