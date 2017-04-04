'''
Bullet.py

implements the Bullet class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import math
from GameObject import GameObject

class Bullet(GameObject):
    speed = 25
    time = 50 * 2 # last 2 seconds
    size = 10

    def __init__(self, x, y, angle):
        size = Bullet.size
        image = pygame.Surface((Bullet.size, Bullet.size), pygame.SRCALPHA)
        pygame.draw.circle(image, (255, 255, 255), (size // 2, size // 2), size // 2)
        super(Bullet, self).__init__(x, y, image, size // 2)
        vx = Bullet.speed * math.cos(math.radians(angle))
        vy = -Bullet.speed * math.sin(math.radians(angle))
        self.velocity = vx, vy
        self.timeOnScreen = 0

    def update(self, screenWidth, screenHeight):
        super(Bullet, self).update(screenWidth, screenHeight)
        self.timeOnScreen += 1
        if self.timeOnScreen > Bullet.time:
            self.kill()
