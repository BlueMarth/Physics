''' a simulation to show the motion of a box sliding under a constant force'''

import pygame as pg
from pygame.locals import *


SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
FPS = 60

MASS = 100 # units
SPRING = 1 # units
DAMPER = 0 # units
    
def updatePosition(delta_x, delta_t):
    acc = delta_x**2 / delta_t**2
    vel = delta_x / delta_t
    new_x = 1/SPRING * (MASS * acc - DAMPER * vel)
    return new_x



''' initial conditions '''
x = 2000
x_mid = 480
x_real = x_mid + x
delta_x = 0

x_real = 700
x_midline = 480 # mid point is x = 480
x_diff_new = x_real - x_midline # = 120 in this case
x_diff_old = x_diff_new
y = 300 # fixed
delta_x = 0


seconds = 4 # simulation duration

while True:
    
    seconds -= 1/FPS # decrease timer

    screen.fill('black')
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        
        # elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:

    

    x_diff_new = updatePosition(delta_x, 1/FPS)
    
    pg.draw.circle(screen, 'green', (x_real, y), 10)
    print(int(x_real))

    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption("fps: " + str(clock.get_fps()))