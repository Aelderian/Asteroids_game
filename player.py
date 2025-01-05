from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame
from shoot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        CircleShape.__init__(self,x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.fire_rate = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.fire_rate -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.fire_rate <= 0:
                self.shoot()


    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shoot = Shot(self.position.x,self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shoot.velocity = forward * PLAYER_SHOOT_SPEED
        self.fire_rate = PLAYER_SHOOT_COOLDOWN









