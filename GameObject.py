'''
GameObject.py

implements the base GameObject class, which defines the wraparound motion
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()  # non-rotated version of image
        w, h = image.get_size()
        self.rect = pygame.Rect(x - w / 2, y - w / 2, w, h)
        self.velocity = (0, 0)

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x - w / 2, self.y - w / 2, w, h)

    def update(self, screenWidth, screenHeight):
        vx, vy = self.velocity
        self.x += vx
        self.y += vy
        self.updateRect()
        # wrap around, and update the rectangle again
        if self.rect.left > screenWidth:
            self.x -= screenWidth
        elif self.rect.right < 0:
            self.x += screenWidth
        if self.rect.top > screenHeight:
            self.y -= screenHeight
        elif self.rect.bottom < 0:
            self.y += screenHeight
        self.updateRect()
