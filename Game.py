'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
from Ship import Ship
from Asteroid import Asteroid
from pygamegame import PygameGame
import random


class Game(PygameGame):
    def init(self):
        Ship.init()
        self.ship = Ship(self.width / 2, self.height / 2)
        self.shipGroup = pygame.sprite.Group(self.ship)

        Asteroid.init()
        self.asteroids = pygame.sprite.Group()
        for i in range(5):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.asteroids.add(Asteroid(x, y))

    def timerFired(self, dt):
        self.shipGroup.update(self.isKeyPressed, self.width, self.height)
        self.asteroids.update(self.width, self.height)

        for ship in pygame.sprite.groupcollide(
            self.shipGroup, self.asteroids, True, False,
            pygame.sprite.collide_circle):
            self.shipGroup.add(Ship(self.width / 2, self.height / 2))

    def redrawAll(self, screen):
        self.shipGroup.draw(screen)
        self.asteroids.draw(screen)

Game(800, 500).run()
