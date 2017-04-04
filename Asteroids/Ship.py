'''
Ship.py

implements the Ship class, which defines the player controllable ship
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import math
from GameObject import GameObject


class Ship(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...
    @staticmethod
    def init():
        Ship.shipImage = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/spaceship.png').convert_alpha(),
            (60, 100)), -90)

    def __init__(self, x, y):
        super(Ship, self).__init__(x, y, Ship.shipImage, 30)
        self.power = 1
        self.drag = 0.9
        self.angleSpeed = 5
        self.angle = 0  # starts pointing straight up
        self.maxSpeed = 20
        self.invincibleTime = 1500
        self.timeAlive = 0

    def update(self, dt, keysDown, screenWidth, screenHeight):
        self.timeAlive += dt

        if keysDown(pygame.K_LEFT):
            self.angle += self.angleSpeed

        if keysDown(pygame.K_RIGHT):
            # not elif! if we're holding left and right, don't turn
            self.angle -= self.angleSpeed

        if keysDown(pygame.K_UP):
            self.thrust(self.power)
        else:
            vx, vy = self.velocity
            self.velocity = self.drag * vx, self.drag * vy

        super(Ship, self).update(screenWidth, screenHeight)

    def thrust(self, power):
        angle = math.radians(self.angle)
        vx, vy = self.velocity
        # distribute the thrust in x and y directions based on angle
        vx += power * math.cos(angle)
        vy -= power * math.sin(angle)
        speed = math.sqrt(vx ** 2 + vy ** 2)
        if speed > self.maxSpeed:
            factor = self.maxSpeed / speed
            vx *= factor
            vy *= factor
        self.velocity = (vx, vy)

    def isInvincible(self):
        return self.timeAlive < self.invincibleTime
