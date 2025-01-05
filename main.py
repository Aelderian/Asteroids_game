# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shoot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    Gamefps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    Shot.containers = (drawable, updatable, shots)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroidsField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0, 0, 0))

        # player.draw(screen)
        # player.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print(f"Game over")
                sys.exit()

            for shot in shots:
                if shot.collide(asteroid):
                    asteroid.split()
                    shot.kill()



        pygame.display.flip()

        dt = Gamefps.tick(60) / 1000


if __name__ == "__main__":
    main()