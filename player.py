import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = pygame.sprite.Group()
        self.TIMER = 0

    def draw(self, screen):
        white = (255, 255, 255)
        points = self.triangle()
        pygame.draw.polygon(screen, white, points, width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.TIMER -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Handle shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shots_group.update(dt)

    def shoot(self):
        # Create a new shot at the player's position and direction
        if self.TIMER <= 0:
            print(f"Player Rotation (shooting): {self.rotation}")
            shot = Shot(self.position, self.rotation)
            # Add the shot to the shots group
            self.shots_group.add(shot)
            self.TIMER = 0.3

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
