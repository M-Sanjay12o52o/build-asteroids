import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(dt)
        updatable.update(dt)

        # asteroid descrution
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # Fill the screen with black background
        screen.fill("black")

        # Draw the player
        # player.draw(screen)
        # drawable.draw(screen)
        # for sprite in drawable:
        # sprite.draw(screen)

        # Draw shots separately if you want additional styling
        # player.shots_group.update(dt)
        # player.shots_group.draw(screen)

        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Calculate the delta time for smoother movement (if needed)
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
