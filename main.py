import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)  

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(dt)
        updatable.update(dt)

        # Fill the screen with black background
        black = (0, 0, 0)
        screen.fill(black)

        # Draw the player
        # player.draw(screen)
        # drawable.draw(screen)
        for sprite in drawable:
          sprite.draw(screen)

        # Update the display
        pygame.display.flip()

        # Calculate the delta time for smoother movement (if needed)
        dt = clock.tick(60) / 1000.0
        print(f"Delta time: {dt:.3f} seconds")


if __name__ == "__main__":
    main()
