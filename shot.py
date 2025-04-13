import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED

SHOT_RADIUS = 5


class Shot(CircleShape):
    def __init__(self, position, direction):
        # Call the parent constructor for CircleShpape (which will set up the rect)
        super().__init__(position.x, position.y, SHOT_RADIUS)

        # Start with a vector pointing downwards (0, 1)
        self.velocity = pygame.Vector2(0, 1)

        # Rotate the velocity to match the player's direction
        self.velocity = self.velocity.rotate(direction)

        # Scale the velocity by the shooting speed
        self.velocity *= PLAYER_SHOOT_SPEED

        print(f"Velocity of shot: {self.velocity}")

    def update(self, dt):
        # Update the shot's position based on its velocity
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.rect.center, self.radius)
