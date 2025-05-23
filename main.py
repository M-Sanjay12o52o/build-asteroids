import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = (0, 255, 0)  # Green color for the button
        self.font = pygame.font.Font(None, 40)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.action:
                self.action()  # Call the action if defined


def start_game():
    global start
    start = True


def restart_game():
    global start
    start = False
    main()


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
    AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    global start
    start = False

    start_button = Button(
        SCREEN_WIDTH / 2 - 100,
        SCREEN_HEIGHT / 2 - 50,
        200,
        50,
        "Start Game",
        start_game,
    )
    restart_button = Button(
        SCREEN_WIDTH / 2 - 100,
        SCREEN_HEIGHT / 2 - 50,
        200,
        50,
        "Restart Game",
        restart_game,
    )

    while not start:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_button.check_click(event.pos)

        start_button.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    while start:
        # Fill the screen with black background
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                restart_button.check_click(event.pos)

        # player.update(dt)
        updatable.update(dt)

        # asteroid descrution
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over you are done!")
                start = False
                break

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Calculate the delta time for smoother movement (if needed)
        dt = clock.tick(60) / 1000.0

        if not start:
            restart_button.draw(screen)
            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    main()
