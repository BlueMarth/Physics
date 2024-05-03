''' a simulation to show the motion of a box sliding under a constant force'''

import pygame as pg
from pygame.locals import *


SIZE = (960, 300)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

mass = 100 # units
spring = 2 # units
damper = 16 # units


def updateAcceleration(x, vel):
    acc = -(spring * x + damper * vel) / mass
    return acc
    
def updateVelocity(old_v, acc):
    new_v = old_v + acc
    return new_v

def updatePosition(old_x, v):
    new_x = old_x + v
    return new_x


# mid point is x = 480
x_real = 900
x_midline = 480
x = x_real - x_midline # = 420 in this case
y = 150 # fixed
vel = 0 # initial velocity set to zero
acc = 0 # initial acceleration unknown

seconds = 0 # simulation duration
bounce = False # set to True if you want it to bounce off the invisible midline wall
seconds = 4

while True and seconds > 0:
    
    seconds -= 1/fps # increment timer

    screen.fill('black')
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        
        elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            x = 420

    x_real = x + x_midline
    if bounce and (x_real < x_midline):
        vel = -vel
    pg.draw.circle(screen, 'green', (x_real, y), 10)
    x = updatePosition(x,vel)
    vel = updateVelocity(vel, acc)
    acc = updateAcceleration(x, vel)
            
    print(int(x))

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))