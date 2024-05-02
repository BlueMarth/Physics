''' a simulation to show the motion of a box sliding under a constant force'''

import pygame as pg
from pygame.locals import *


SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

mass = 100 # units
damper = 25 # units
spring = 0.5 # units

def updateForce(mass, damper, spring, x_diff, vel, acc):
    force = mass * acc - damper * vel - spring * x_diff
    return force

def updateAcceleration(force):
    force = updateForce(mass, damper, spring, x_diff, vel, acc)
    return force / mass
    
def updateVelocity(old_v, acc):
    new_v = old_v + acc
    return new_v

def updatePosition(old_x, v):
    new_x = old_x + v
    return new_x
    
    

# mid point is x = 480
x_real = 900
x_midline = 480
x_diff = x_real - x_midline # = 420 in this case
y = 300 # fixed
vel = 0 # initial velocity set to zero
acc = 0 # initial acceleration unknown
force = 0 # initial force unknown

seconds = 4 # simulation duration

while True:
    
    seconds -= 1/fps # decrease timer

    screen.fill('black')
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        
        # elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:

    x_real = x_diff + x_midline
    pg.draw.circle(screen, 'green', (x_real, y), 10)
    x_diff = updatePosition(x_diff,vel)
    vel = updateVelocity(vel, acc)
    acc = updateAcceleration(force)
            
    print(int(x_diff))

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))