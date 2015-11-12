'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15

use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT

- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''


import pygame


class PygameGame(object):

    def init(self):
        print("Initializing the game...")

    def mousePressed(self, x, y):
        print("Clicked the mouse at (%d, %d)" % (x, y))

    def mouseReleased(self, x, y):
        print("Released the mouse at (%d, %d)" % (x, y))

    def mouseMotion(self, x, y):
        print("The mouse moved to (%d, %d)" % (x, y))

    def mouseDrag(self, x, y):
        print("The mouse was dragged to (%d, %d)" % (x, y))

    def keyPressed(self, keyCode, modifier):
        print("The key with code %d was pressed" % keyCode)
        print("\tmodifier: %r" % modifier)

    def keyReleased(self, keyCode, modifier):
        print("The key with code %d was released" % keyCode)
        print("\tmodifier: %r" % modifier)

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self.keys.get(key, False)

    def __init__(self, width=600, height=400, fps=40, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title

    def run(self):
        pygame.init()

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self.keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self.keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self.keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
