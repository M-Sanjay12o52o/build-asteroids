import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Create screen with width and height from constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the player's position to the center of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Instantiate the player object
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)

        # Fill the screen with black background
        black = (0, 0, 0)
        screen.fill(black)

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Calculate the delta time for smoother movement (if needed)
        dt = clock.tick(60) / 1000.0
        print(f"Delta time: {dt:.3f} seconds")


if __name__ == "__main__":
    main()
