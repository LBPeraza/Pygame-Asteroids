'''
Explosion.py

implements the Explosion class
Lukas Peraza, 2016 for 15-112 Pygame Lecture
'''
import pygame

class Explosion(pygame.sprite.Sprite):
    @staticmethod
    def init():
        image = pygame.image.load('images/explosion.png')
        rows, cols = 5, 5
        width, height = image.get_size()
        cellWidth, cellHeight = width / cols, height / rows
        Explosion.frames = []
        for i in range(rows):
            for j in range(cols):
                subImage = image.subsurface(
                    (j * cellWidth, i * cellHeight, cellWidth, cellHeight))
                Explosion.frames.append(subImage)


    def __init__(self, x, y):
        super(Explosion, self).__init__()

        self.x, self.y = x, y
        self.frame = 0
        self.frameRate = 20
        self.aliveTime = 0

        self.updateImage()

    def updateImage(self):
        self.image = Explosion.frames[self.frame]
        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, dt):
        self.aliveTime += dt
        self.frame = self.aliveTime // (1000 // self.frameRate)
        if self.frame < len(Explosion.frames):
            self.updateImage()
        else:
            self.kill()
