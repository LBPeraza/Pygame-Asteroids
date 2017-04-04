import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def init(data):
    data.circles = []
    data.message = "Pygame events example"
    data.font = pygame.font.Font(None, 30)

def keyPressed(data, key):
    if key == pygame.K_d and len(data.circles) > 0:
        (x, y, *_) = data.circles.pop(0)
        data.message = "Deleted a circle from (%d, %d)" % (x, y)

def mousePressed(data, x, y):
    data.circles.append((x, y, random.randint(10, 30),
        random.choice([RED, GREEN, BLUE]),
        random.choice([RED, GREEN, BLUE, BLACK])))
    data.message = "Mouse pressed at (%d, %d)" % (x, y)

def mouseMoved(data, buttons, x, y):
    action = "moved" if buttons == (0, 0, 0) else "dragged"
    data.message = "Mouse %s to (%d, %d)" % (action, x, y)

def drawMessage(data, screen):
    text = data.font.render(data.message, True, BLACK)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                        screen.get_height() - text.get_height() * 2))

def drawCircle(screen, x, y, r, color, outline):
    pygame.draw.circle(screen, color, (x, y), r)
    pygame.draw.circle(screen, outline, (x, y), r + 2, 5)

def redrawAll(data, screen):
    for circle in data.circles:
        drawCircle(screen, *circle)
    drawMessage(data, screen)

pygame.init()
clock = pygame.time.Clock()
# create the display surface
screen = pygame.display.set_mode((500, 300))

playing = True

class Struct(object): pass
data = Struct()

init(data)

while playing:
    time = clock.tick(50) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            keyPressed(data, event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePressed(data, *event.pos)
        elif event.type == pygame.MOUSEMOTION:
            mouseMoved(data, event.buttons, *event.pos)

    screen.fill(WHITE)
    redrawAll(data, screen)
    pygame.display.flip()

pygame.quit()