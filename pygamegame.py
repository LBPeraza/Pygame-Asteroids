
import pygame as pg


class PygameGame(object):

    '''
    a bunch of stuff is left out in this post, but you can see it in the Github
    repo ()
    '''

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

    def __init__(self, width=600, height=400, fps=40):
        self.width = width
        self.height = height
        self.fps = fps

    def run(self):
        pg.init()

        clock = pg.time.Clock()
        screen = pg.display.set_mode((self.width, self.height))

        # stores all the keys currently being held down
        self.keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pg.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pg.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pg.KEYDOWN:
                    self.keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pg.KEYUP:
                    self.keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pg.QUIT:
                    playing = False
            self.redrawAll(screen)
            pg.display.flip()

        pg.quit()
