# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
   # asteroidfield = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for object in asteroids:
            if object.collision(player):
                sys.exit("Game over!")
        for asteroid in asteroids:
            asteroid.update(dt)
            asteroid.draw(screen)
        for object in asteroids:
            for bullet in shots:
                if bullet.collision(object):
                    bullet.kill()
                    object.split(asteroids)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            shot = player.shoot()
            if shot:
                shots.add(shot) # or shots.append(shot) if using a list
        for shot in shots:
            shot.update(dt)
            shot.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
