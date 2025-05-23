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
    Player.containers = (updatable, drawable)
    AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    global start
    start = False
    game_over = False

    start_button = Button(
        SCREEN_WIDTH / 2 - 150,
        SCREEN_HEIGHT / 2 - 50,
        300,
        50,
        "Start Game [Space]",
        start_game,
    )
    restart_button = Button(
        SCREEN_WIDTH / 2 - 150,
        SCREEN_HEIGHT / 2 - 50,
        300,
        50,
        "Restart Game [r]",
        restart_game,
    )
    quit_button = Button(
        SCREEN_WIDTH / 2 - 150,
        SCREEN_HEIGHT / 2 + 70,
        300,
        50,
        "Quit [q]",
        lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
    )
    quit_button.color = (255, 0, 0)

    exit_button = Button(
        SCREEN_WIDTH / 2 - 100,
        SCREEN_HEIGHT / 2 + 70,
        300,
        50,
        "Exit [x]",
        lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
    )
    exit_button.color = (255, 0, 0)

    running = True
    # while not start:
    while running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                # sys.exit()
                running = False

            if not start:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start_button.check_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        start_game()
            elif game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    restart_button.check_click(event.pos)
                    quit_button.check_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r or event.key == pygame.K_RETURN:
                        restart_game()
                    elif event.key == pygame.K_q:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

        if not start:
            start_button.draw(screen)
        elif start and not game_over:
            # Game running logic
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    print("Game over!")
                    game_over = True  # Set game_over to True
                    # You might want to stop player movement or clear asteroids here
                    # For a full restart, you'd re-initialize game elements
                    break  # Break out of inner loop to prevent multiple game over messages

                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()

            for obj in drawable:
                obj.draw(screen)
        elif game_over:
            # Game over screen
            font = pygame.font.Font(None, 60)
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)
            )
            screen.blit(game_over_text, text_rect)
            restart_button.draw(screen)
            quit_button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    pygame.quit()  # It's generally good practice to call pygame.quit() when your program truly ends
    sys.exit()  # And sys.exit() to ensure the Python script terminates


if __name__ == "__main__":
    main()
