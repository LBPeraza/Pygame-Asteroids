'''
Game.py

Actually implements the game
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame
from Ship import Ship
from pygamegame import PygameGame


class Game(PygameGame):
    def init(self):
        Ship.init()
        self.ship = Ship(self.width / 2, self.height / 2)
        self.shipGroup = pygame.sprite.Group(self.ship)

    def timerFired(self, dt):
        self.shipGroup.update(self.isKeyPressed, self.width, self.height)

    def keyPressed(self, code, mod):
        pass

    def redrawAll(self, screen):
        self.shipGroup.draw(screen)

Game(600, 600).run()
