'''
Asteroid.py

implements the Asteroid class
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
import random
from GameObject import GameObject


class Asteroid(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load('images/asteroids.png').convert_alpha()
        rows, cols = 4, 4
        width, height = image.get_size()
        cellWidth, cellHeight = width / cols, height / rows
        Asteroid.images = []
        for i in range(rows):
            for j in range(cols):
                subImage = image.subsurface(
                    (i * cellWidth, j * cellHeight, cellWidth, cellHeight))
                Asteroid.images.append(subImage)

    minSize = 2
    maxSize = 6
    maxSpeed = 5

    def __init__(self, x, y, level=None):
        if level is None:
            level = random.randint(Asteroid.minSize, Asteroid.maxSize)
        self.level = level
        factor = self.level / Asteroid.maxSize
        image = random.choice(Asteroid.images)
        w, h = image.get_size()
        image = pygame.transform.scale(image, (int(w * factor), int(h * factor)))
        super(Asteroid, self).__init__(x, y, image, w / 2 * factor)
        self.angleSpeed = random.randint(-10, 10)
        vx = random.randint(-Asteroid.maxSpeed, Asteroid.maxSpeed)
        vy = random.randint(-Asteroid.maxSpeed, Asteroid.maxSpeed)
        self.velocity = vx, vy

    def update(self, screenWidth, screenHeight):
        self.angle += self.angleSpeed
        super(Asteroid, self).update(screenWidth, screenHeight)

    def breakApart(self):
        if self.level == Asteroid.minSize:
            return []
        else:
            return [Asteroid(self.x, self.y, self.level - 1),
                    Asteroid(self.x, self.y, self.level - 1)]
