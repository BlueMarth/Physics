''' a simulation to show the motion of a box sliding under a constant force'''

import pygame as pg
from pygame.locals import *


SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

force = 0 # units
mass = 1000 # units
damper = 25 # units
spring = 0.2 # units

acc_per_sec = force / mass # pixel per second squared
acc_per_frame = acc_per_sec / fps # pixel per second per 16.7 ms

def updateForce(mass, damper, spring, rel_x, vel, acc):
    force = mass * acc - damper * vel - spring * rel_x
    return force

def updateAcceleration(force):
    force = updateForce(mass, damper, spring, rel_x, v, acc)
    return force / mass
    
def updateVelocity(old_v, acc):
    new_v = old_v + acc
    return new_v

def updatePosition(old_x, v):
    new_x = old_x + v
    return new_x
    
    

# mid point is x = 480
x = 480
rel_x = 0
y = 300
v = 100
acc = __
force = 0


seconds = 4

while True and seconds > 0:
    seconds -= 1/fps
    screen.fill('black')
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        # elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
    
    force = updateForce(mass, damper, spring, rel_x, v, acc)

    x = rel_x + 480
    pg.draw.circle(screen, 'green', (x, y), 10)

    rel_x = x - 480    
    rel_x = updatePosition(x,v)
    v = updateVelocity(v, acc)
    acc = updateAcceleration(force)
    
    
    print(int(rel_x))

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))