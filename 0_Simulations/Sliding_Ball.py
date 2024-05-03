''' a simulation to show the motion of a ball sliding at constant speed vs under a constant appled force '''

import pygame as pg
from pygame.locals import *


SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 50

force = 100 # units
mass = 100 # units
acc_per_sec = 2 # pixel per second squared
acc_per_frame = acc_per_sec / fps # pixel per second per 16.7 ms

def updateVelocity(old_v, acc):
    new_v = old_v + acc
    return new_v

def updatePosition(old_x, v):
    new_x = old_x + v
    return new_x
    

x = 30
y = 300
v = 0
x1 = 0
seconds = 0

while True:
    
    screen.fill('black')
    
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        # elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
    
    # accelerating sled
    pg.draw.circle(screen, 'green', (x, 200), 10)
    v = updateVelocity(v, acc_per_frame)
    x = updatePosition(x, v)
    
    # uniform speed sled
    pg.draw.circle(screen, 'red', (x1, 400), 10)
    v1 = 3
    x1 = updatePosition(x1, v1)
    
    print(int(x),int(v), int(x1), int(v1))

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))