'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
from Ship import Ship
from Asteroid import Asteroid
from Bullet import Bullet
from pygamegame import PygameGame
import random


class Game(PygameGame):
    def init(self):
        self.bgColor = (0, 0, 0)
        Ship.init()
        ship = Ship(self.width / 2, self.height / 2)
        self.shipGroup = pygame.sprite.Group(ship)

        Asteroid.init()
        self.asteroids = pygame.sprite.Group()
        for i in range(5):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.asteroids.add(Asteroid(x, y))

        self.bullets = pygame.sprite.Group()

    def keyPressed(self, code, mod):
        if code == pygame.K_SPACE:
            ship = self.shipGroup.sprites()[0]
            self.bullets.add(Bullet(ship.x, ship.y, ship.angle))

    def timerFired(self, dt):
        self.shipGroup.update(self.isKeyPressed, self.width, self.height)
        self.asteroids.update(self.width, self.height)
        self.bullets.update(self.width, self.height)

        if pygame.sprite.groupcollide(
            self.shipGroup, self.asteroids, True, False,
            pygame.sprite.collide_circle):
            self.shipGroup.add(Ship(self.width / 2, self.height / 2))

        for asteroid in pygame.sprite.groupcollide(
            self.asteroids, self.bullets, True, True,
            pygame.sprite.collide_circle):
            self.asteroids.add(asteroid.breakApart())

    def redrawAll(self, screen):
        self.shipGroup.draw(screen)
        self.asteroids.draw(screen)
        self.bullets.draw(screen)

Game(800, 500).run()
