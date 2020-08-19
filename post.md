Pygame is a set of python modules designed for creating games. It's built on top of the SDL Libraries, which give much better performance than any fully-Python application. This lets us create fully-featured games and multimedia projects directly in Python.

-----

-----

#### Introduction

##### Why Pygame?
In 112, we teach you how to use tkinter, the standard Python graphics library. So why should you use Pygame over that?

**Pros:**

- It's faster than tkinter
- You can use images more robustly
- You get a lot more control over the event loop

**Cons:**

 - It's a bit more complicated to learn
 - It's not installed with Python
 - We don't teach it to you in 112

So ultimately, it's up to you whether you want to use Pygame or not. Lots of projects turn out great using tkinter, and lots of other projects turn out badly in Pygame. But the best Pygame projects are better than the best tkinter projects.

-----

##### Pygame Examples

Here are some examples of 112 term projects written in Pygame, for motivation.

- [Poly X](https://youtu.be/VEIStlH-OpQ?t=21)
- [Moderately Impressive Apparatus](https://youtu.be/O6L3qzDt4o0?t=39)
- [Super Smash 112](https://youtu.be/NStf35ilGog?t=120)

-----

-----

#### Using Pygame

##### Surfaces

What is a Surface?

- A Pygame object for representing images
- You can think of it as a collection of pixels

The display is a Surface. We can clear the display by calling `.fill` on the display surface:

~~~python
screen.fill((r, g, b)) # not specific to screens - you can do this on any surface
~~~

A surface can be drawn onto another surface using `blit`.

~~~python
surface.blit(source, dest, area=None)
~~~

`blit` copies the pixels from `source` (another surface) onto `surface`. `dest` is a Pygame Rect object or a tuple describing where to copy the pixels on to.

The optional argument `area` describes where on the source to copy pixels from. If `None` is specified, it will copy the entire source.

[Surface Reference](http://www.pygame.org/docs/ref/surface.html)

We can also use the `pygame.transform` module to perform really helpful transformations to Surfaces - things like rotating, flipping, scaling, etc.

~~~python
pygame.transform.rotate(surface, angle) # angle is in degrees
pygame.transform.flip(surface, xbool, ybool)
pygame.transform.scale(surface, (width, height), dest=None)
~~~
If `dest` is given in `scale`, it must be a surface with the same width and height specified.

**IMPORTANT NOTE about rotating:**

Surfaces are *always* rectangles, so if you rotate a surface by something other than an increment of 90 degrees, it will increase in size. Usually it's better to keep an unrotated version of your surface and then rotate it before you draw. For example:

[Transform Reference](https://www.pygame.org/docs/ref/transform.html)

~~~python
surf = pygame.Surface((100, 200))
for angle in range(360):
    rotatedSurf = pygame.transform.rotate(surf, angle)
~~~
is MUCH better than

~~~python
surf = pygame.Surface((100,200))
for i in range(360):
    surf = pygame.transform.rotate(surf, 1)
~~~

-----

##### Main Loop

Each Pygame game always starts with some initialization code:

~~~python
import pygame
pygame.init()
clock = pygame.time.Clock()
# create the display surface
screen = pygame.display.set_mode((width, height))
~~~

Then after the initialization, there is always one main loop:

~~~python
playing = True
while playing:
    time = clock.tick(fps) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
pygame.quit()
~~~

-----

##### Events

Of course, this main loop doesn't create a very exciting game if we don't allow for some interaction! This is where events come in. There are a bunch of different types of events in Pygame. Here are the few you should care about, along with their attributes:

- `QUIT`
- `KEYDOWN`
     - `unicode`: a string representation of the key pressed
     - `key`: the code of the key pressed (more useful, since `KEYUP` only has this)
     - `mod`: modifier keys being held - stored as an int with bits set per modifier key
- `KEYUP`
     - `key`: same as above
     - `mod`: same as above
- `MOUSEBUTTONDOWN`
     - `pos`: (x, y) position of the click
     - `button`: an int representing which mouse button was clicked (1 for left mouse, 2 and 3 depend on OS)
- `MOUSEBUTTONUP`
     - `pos`: same as above
     - `button`: same as above
- `MOUSEMOTION`
     - `pos`: same as above
     - `rel`: position change since last mouse position
     - `buttons`: a tuple where the `(i-1)` index is 1 if the `i`th button is being held (as defined above)

As we saw in the game loop section above, we can get all the events by calling `pygame.event.get()` - this gives us all the events which have occurred since the last time we called it. We can then loop over all these events and call our `mousePressed` and `keyPressed` functions. For example:

~~~python
def mousePressed(event):
    print(event.pos)

'''
initialization stuff here
'''
while playing:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePressed(event)
~~~

It's important to note that `event.code` in a `KEYDOWN` or `KEYUP` event is an integer representing the key being pressed. However, we don't need to know exactly which key maps to which integer - Pygame does that for us! For example, if we want to check for the up and down arrow keys:

~~~python
def keyPressed(event):
    if event.key == pygame.K_DOWN:
        print("You pressed the down arrow!")
    elif event.key == pygame.K_UP:
        print("You pressed the up arrow!")
~~~

There is similar functionality for modifier keys (shift, ctrl, command, etc.).

[Events Example](https://github.com/LBPeraza/Pygame-Asteroids/blob/master/Examples/EventsExample.py)

[Key Reference](http://www.pygame.org/docs/ref/key.html)

[Event Reference](http://www.pygame.org/docs/ref/event.html)

-----

##### Drawing and Images

So we can get all the events, but we still can't see anything. Still sounds like a pretty bad game.

We saw earlier that we can copy the pixels of one Surface onto another, but how do we get the pixels to be what we want? That's where the `pygame.draw` module comes in!

`pygame.draw` gives us a bunch of primitive drawing functions (think `canvas.create_rectangle`, `canvas.create_oval`, etc.) that we can use to draw onto an arbitrary Surface.

~~~python
pygame.draw.rect(surface, color, Rect, width=0)
pygame.draw.circle(surface, color, position, r, width=0)
pygame.draw.ellipse(surface, color, Rect, width=0)
pygame.draw.arc(surface, color, Rect, start_angle, stop_angle, width=1)
pygame.draw.line(surface, color, start_pos, end_pos, width=1)
~~~
Where `Rect` is an argument, it is either

- A tuple of `(left, top, width, height)` or `((left, top), (width, height))`
- A `pygame.Rect` object (defined with the same parameters)

[Drawing Reference](https://www.pygame.org/docs/ref/draw.html)

In Pygame, working with images is as simple as loading the images onto surfaces and then just using it as a normal surface. These are the functions you probably want:

~~~python
pygame.image.load(filename) # returns the surface with the image
pygame.image.save(surface, filename) # saves the surface into an image
~~~

After loading the image onto a surface, you may want to preserve transparency from the image, so a full image load would look like:

~~~python
imageSurf = pygame.image.load('image.png').convert_alpha()
~~~

Now, since the image is a Surface, we can transform it or draw onto it just like any other surfaces!

[Image Reference](https://www.pygame.org/docs/ref/image.html)

One last thing to note about drawing - whenever we draw something onto the `screen`, either by `blit`ing, or drawing directly on the `screen` Surface, the display must be updated. There are three ways to do this:

~~~python
pygame.display.flip()
pygame.display.update(Rect)
pygame.display.update(rectlist)
~~~

`flip` updates the entire display

`update(Rect)` updates the part of the screen covered by `Rect`

`update(rectlist)` updates the part of the screen covered by any rectangle in `rectlist`

-----

##### Framework

This notion of events and boilerplate code motivates a framework similar to the one we've used in 112 so far (you know, `run` with tkinter). Therefore, I've created a Pygame analog to the framework you're used to.

I highly encourage using this framework, or something similar, in your term project, if you're using Pygame! A few disclaimers, though:

- It uses OOP, so you'll be extending the framework, not just writing `mousePressed`, `keyPressed`, etc.
- The syntax will obviously be different (Pygame vs. tkinter)
- You absolutely MUST cite it if you use this!
- You can edit it however much you want to add functionality. Have fun!

~~~python
import pygame


class PygameGame(object):

    """
    a bunch of stuff is left out of this file, but you can check it out in the Github repo
    """

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

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
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill((255, 255, 255))
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()
~~~

We'll create an actual game with this framework in a few minutes!

-----

##### Sprites

Sprites are probably one of the most important parts of using Pygame. They aren't strictly *necessary*, but they can make your code **simpler** (cool) and **faster** (awesome!).

The `pygame.sprite.Sprite` class is a base class which gives basic functionality for game objects. Some functionality it provides by default:

- Batch rectangular and circular collision detection
- Batch updates
- Batch drawing

Some general steps for using Sprites

1. Extend the `pygame.sprite.Sprite` class
2. Call the superclass's __init__ method
3. Create the `update` method
4. Assign the `rect`, `image`, and optionally the `radius` attributes
    - `rect` is used for drawing (position / size) and rectangular collision detection
    - `image` is used for drawing: it's a Surface
    - `radius` is used for circular collision detection
5. Add instances of your subclass into Groups

So what is a Group? A Group (`pygame.sprite.Group`) is an object which represents a collection of Sprites. You can use groups to update each sprite in the group at the same time, or to draw each sprite in the group at the same time.

Perhaps the coolest built-in functionality of Groups, however, is the `pygame.sprite.groupcollide` function. This allows you to specify two groups, and determine if any sprite from the first group is colliding with any sprite in the second group. We can specify lots of things for this:

- The two groups we want to check (`group1` and `group2`)
- `dokill1` and `dokill2`: if one of these is True, any colliding Sprites in the respective group are removed automatically. This means no more confusing list modifications!
- `collided`: this is a function which takes two Sprites and tells if they're colliding - this means we can specify how to detect collisions between groups. Use `pygame.sprite.collide_rect`, `pygame.sprite.collide_circle`, or a custom collision function!

`collidegroup` returns a `Sprite_Dict` object - this is a dictionary which maps Sprites from `group1` to all the Sprites in `group2` that it was colliding with. This allows us to do any necessary cleanup code for the removed objects.

Here's a quick Sprite example using Dots:

~~~python
class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Dot, self).__init__()
        self.radius = random.randint(5, 20)
        self.x, self.y = x, y
        self.xSpeed = random.randint(-10, 10)
        self.ySpeed = random.randint(-10, 10)
        self.rect = pygame.Rect(x - self.radius, y - self.radius,
                                2 * self.radius, 2 * self.radius)
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.circle(self.image, (r, g, b),
                           (self.radius, self.radius), self.radius)

    def getRect(self):  # GET REKT
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                2 * self.radius, 2 * self.radius)

    def update(self, screenWidth, screenHeight):
        self.x += self.xSpeed
        self.y += self.ySpeed
        if self.x < 0:
            self.x = screenWidth
        elif self.x > screenWidth:
            self. x = 0
        if self.y < 0:
            self.y = screenHeight
        elif self.y > screenHeight:
            self.y = 0
        self.getRect()

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

dots = pygame.sprite.Group()
playing = True
while playing:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            d = Dot(*event.pos)
            dots.add(d)
        elif event.type == pygame.QUIT:
            playing = False
    dots.update(500, 500)
    screen.fill((255, 255, 255))
    dots.draw(screen)
    pygame.display.flip()
pygame.quit()
~~~

[Sprite Reference](https://www.pygame.org/docs/ref/sprite.html)

-----

-----

#### Asteroids

So now that we've learned about Pygame, let's write a game! We're going to write Asteroids. If you don't know what Asteroids is, [this video](https://www.youtube.com/watch?v=WYSupJ5r2zo) is the original version. Since we're using Pygame, though, we can make it look much better!

Let's start by getting some pictures for the ship and asteroids. Through some Google-Fu, I was able to find these:

![SPACE SHIP WOO](Asteroids/images/spaceship.png)

![ASTEROIDS KERBLANG](Asteroids/images/asteroids.png)

We can load these images in and use them as our graphics. The asteroids are cool since they're on a grid - we can use the `pygame.Surface.subsurface` method to grab each individual asteroid, then pick a random one for each individual asteroid.

So let's start writing code!

-----

##### Game Objects

One thing that we might notice is that every object in the game (Ship, Asteroids, Bullets) all move in a similar fashion - that is, they all have some velocity (the ship's velocity changes from user input, but it exists), and they all wrap around the edges when they reach an edge. So we can implement this as our base `GameObject` class. In `GameObject.py`, let's make this class.

~~~python
'''
GameObject.py

implements the base GameObject class, which defines the wraparound motion
Lukas Peraza, 2015 for 15-112 Pygame Lecture
'''
import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()  # non-rotated version of image
        w, h = image.get_size()
        self.updateRect()
        self.velocity = (0, 0)
        self.angle = 0

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, screenWidth, screenHeight):
        self.image = pygame.transform.rotate(self.baseImage, self.angle)
        vx, vy = self.velocity
        self.x += vx
        self.y += vy
        self.updateRect()
        # wrap around, and update the rectangle again
        if self.rect.left > screenWidth:
            self.x -= screenWidth + self.width
        elif self.rect.right < 0:
            self.x += screenWidth + self.width
        if self.rect.top > screenHeight:
            self.y -= screenHeight + self.height
        elif self.rect.bottom < 0:
            self.y += screenHeight + self.height
        self.updateRect()
~~~

Let's break this code apart. First we see that we're extending the `Sprite` class. This is going to give us all that awesome functionality we were talking about!

Then we have the `__init__` method, which takes `x`, `y`, `image`, and `radius`. These are all pretty obvious arguments. The only weird thing happening is that we're copying the image, but this is for the rotating problem. We want to keep an unrotated copy so the image doesn't keep growing!

`updateRect` recomputes the `rect` attribute given new x and y coordinates, and a rotated image.

`update` does the wraparound motion we were talking about before. We can use the `rect` attribute's `left`, `top`, `right`, and `bottom` attributes to great effect here. Awesome!

This class just implements the very basics of motion, but it's actually really helpful, because it means we don't have to do it for every other object!

-----

##### Ship

So now let's make the player's ship! This is clearly going to extend the basic `GameObject` class, which means it's going to also get the awesome stuff from `Sprite` as well. Let's check out `Ship.py`:

~~~python
import pygame
import math
from GameObject import GameObject

class Ship(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...
    @staticmethod
    def init():
        Ship.shipImage = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('images/spaceship.png').convert_alpha(),
            (60, 100)), -90)  # rotate -90 because ship is pointing up, but 0 = right

    def __init__(self, x, y):
        super(Ship, self).__init__(x, y, Ship.shipImage, 30)
        self.power = 1
        self.drag = 0.9
        self.angleSpeed = 5
        self.angle = 0  # starts pointing straight up
        self.maxSpeed = 20

    def update(self, keysDown, screenWidth, screenHeight):
        if keysDown(pygame.K_LEFT):
            self.angle += self.angleSpeed

        if keysDown(pygame.K_RIGHT):
            # not elif! if we're holding left and right, don't turn
            self.angle -= self.angleSpeed

        if keysDown(pygame.K_UP):
            self.thrust(self.power)
        else:
            vx, vy = self.velocity
            self.velocity = self.drag * vx, self.drag * vy

        super(Ship, self).update(screenWidth, screenHeight)

    def thrust(self, power):
        angle = math.radians(self.angle)
        vx, vy = self.velocity
        # distribute the thrust in x and y directions based on angle
        vx += power * math.cos(angle)
        vy -= power * math.sin(angle)
        speed = math.sqrt(vx ** 2 + vy ** 2)
        if speed > self.maxSpeed:
            factor = self.maxSpeed / speed
            vx *= factor
            vy *= factor
        self.velocity = (vx, vy)
~~~

Again, let's break this down.

We see that `shipImage` is stored as a class attribute - this makes sense, as any Ship we create should use the same image, which means we don't have to keep loading it every time we create a new one (which probably won't happen for Ship, but it will for Asteroids!). We also store it by calling the static method `init` - this is because we can't use most of the Pygame functions until after `pygame.init()` is called. We'll call `Ship.init()` in our game's `init` method.

Really, the only other interesting part is `timerFired`. You might ask why this isn't in `keyPressed` - we want smooth motion, so we'll ask our framework whether a key is down, and update velocities based on that every frame!

`thrust` just uses some basic trig to distribute extra velocity in the x and y directions.

-----

##### Let's Play

So now we can test out motion and see how it works! Let's start writing `Game.py`.

~~~python
import pygame
from Ship import Ship
from pygamegame import PygameGame


class Game(PygameGame):
    def init(self):
        Ship.init()
        self.shipGroup = pygame.sprite.Group(Ship(self.width, self.height))

    def timerFired(self, dt):
        self.shipGroup.update(self.isKeyPressed, self.width, self.height)

    def redrawAll(self, screen):
        self.shipGroup.draw(screen)

Game(600, 600).run()
~~~

The only weird part here is that we don't store the ship itself, but rather a Group which the ship is part of. This is so we can call `update`, `draw`, and use `groupcollide` directly on the group.

If we run this, we can move the ship around the screen! It even wraps around, because it's a Game Object. Cool!

Let's do Asteroids now.

-----

##### Asteroids (The Objects, not the Game!)

What functionality do Asteroids need, on top of the GameObject class?

- Get a random image
- Get a random speed
- Be able to break apart into two smaller asteroids (so we need size)

In `Asteroids.py`, let's start writing the `Asteroid` class, which obviously extends `GameObject`.

`Asteroid`'s `init` method is going to be a more complicated than `Ship`'s, because we need to split the asteroid image up. Let's check it out.

~~~python
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
~~~

There are 4 rows and 4 columns in our asteroid 'grid', so we get each individual asteroid by subsampling the Surface 16 times.

Let's also add `minSize` and `maxSize` class attributes to the Asteroid class. These will define the starting size of each asteroid. Also add `maxSpeed` to pick a random asteroid velocity.

~~~python
class Asteroid(GameObject):
    minSize = 2
    maxSize = 4
    maxSpeed = 5
    ''' the init method from above... '''
~~~

Now let's write the rest of the methods.

~~~python
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
~~~

`__init__` is just creating a bunch of randomly initialized variables, and picking a random asteroid image. `breakApart` is the interesting method here. If an asteroid is already only level 1, breaking it makes it disappear, so we return an empty list. Otherwise we return two smaller asteroids.

Now we can add asteroids into our game!

Let's update the methods in our Game class to get Asteroids in it.

~~~python
def init(self):
    # old stuff still here
    Asteroid.init()
    self.asteroids = pygame.sprite.Group()
    for i in range(5):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        self.asteroids.add(Asteroid(x, y))
~~~
Here, we're randomly initializing 5 asteroids.

The other two methods just involve calls to `self.asteroids.update` or `self.asteroids.draw`. I'll let you figure those out.

If we play now, we have asteroids! But running into them doesn't do anything. This is where we'll use `pygame.sprite.groupcollide`! In our `timerFired`, we want to check if the Ship hit any asteroids. If it did, we remove it and create a new ship back at the center. Add this code to `timerFired`.

~~~python
if pygame.sprite.groupcollide(self.shipGroup, self.asteroids,
    True, False,  # remove the ship, but not the asteroid
    pygame.collide_circle):  # check circular collisions, not rectangular
    self.shipGroup.add(Ship(self.width / 2, self.height / 2))
~~~

Now hitting an asteroid causes us to respawn! All that's left is destroying the asteroids, and for that, we'll need a Bullet class.

----

##### Bullets

Our Bullet class is actually really small. First we need to set a velocity based on the angle that it's shot at. Then the GameObject class takes care of most of the rest! All that we have to do is despawn the bullet after it's been on the screen for too long. We can do this by calling the `pygame.sprite.Sprite.kill` method.

~~~python
class Bullet(GameObject):
    speed = 25
    time = 50 * 5 # last 5 seconds
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
~~~

This is it for bullets. Let's add them into the game and we're done!

Add the following to the correct methods:

~~~python
def init(self):
    # old stuff
    self.bullets = pygame.sprite.Group()

def keyPressed(self, keyCode, mod):
    if keyCode == pygame.K_SPACE:
        ship = self.shipGroup.sprites()[0]
        self.bullets.add(Bullet(ship.x, ship.y, ship.angle))

def timerFired(self, dt):
    # other update things
    self.bullets.update(self.width, self.height)
    # other collision stuff
    for asteroid in pygame.sprite.groupcollide(self.asteroids, self.bullets,
        True, True, pygame.sprite.collide_circle):
        self.asteroids.add(asteroid.breakApart())

def redrawAll(self, screen):
    # other drawing things
    self.bullets.draw(screen)
~~~

And now we're done! Let's play the game and have some fun :)

-----

##### Extras

So this game is fun and all, but there's lots of stuff we could add. Here are some suggestions:

- Invincibility when you first spawn / respawn
- Score
- Lives
- Splash Screen
- Power ups
- Sound (use `pygame.mixer`)
- Levels
- Online multiplayer
- Anything else you think would be cool

-----

-----

#### Conclusion

That's it for this post! Here's some extra material you can check out if you want.

##### Other Pygame things

We didn't talk about rendering text or using sound. For text, you'll want to use the `pygame.font` module. For sounds, use `pygame.mixer`. 

[Font Reference](https://www.pygame.org/docs/ref/font.html)

[Mixer Reference](https://www.pygame.org/docs/ref/mixer.html)

-----

##### Links

Code: [https://github.com/LBPeraza/Pygame-Asteroids](https://github.com/LBPeraza/Pygame-Asteroids)

Pygame Docs: [https://www.pygame.org/docs/](https://www.pygame.org/docs/)

Extra Information on Sprites: [http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en#section_13](http://programarcadegames.com/index.php?chapter=introduction_to_sprites&lang=en#section_13)

Possibly more coming soon...
