from circleshape import *
import pygame
from constants import *
import random
from main import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(int(self.position.x), int(self.position.y)),self.radius)

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2
            #asteroid_1.position = pygame.math.Vector2(self.x, self.y)
            #asteroid_2.position = pygame.math.Vector2(self.x, self.y)

            # After setting asteroid_1.position...
            #asteroid_1.position.x = max(0, min(asteroid_1.position.x, SCREEN_WIDTH))
            #asteroid_1.position.y = max(0, min(asteroid_1.position.y, SCREEN_HEIGHT))

            #asteroid_2.position.x = max(0, min(asteroid_2.position.x, SCREEN_WIDTH))
            #asteroid_2.position.y = max(0, min(asteroid_2.position.y, SCREEN_HEIGHT))
            #asteroid_1.x = asteroid_1.position.x
            #asteroid_1.y = asteroid_1.position.y
            #asteroid_2.x = asteroid_2.position.x
            #asteroid_2.y = asteroid_2.position.y

            asteroids.add(asteroid_1)
            asteroids.add(asteroid_2)
      
         