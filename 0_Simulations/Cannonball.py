''' a mini game to shoot cannonballs in a parabolic trajectory'''

import pygame as pg
from pygame.locals import *
import math


SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60

def drawBackground():
    screen.fill('black')
    pg.draw.line(screen, 'red', [0, SEA_LEVEL], [SIZE[0], SEA_LEVEL], 1)

def getDrag(speed_sqrd, angle):
    # if speed_sqrd < 
    drag = 0.5 * DENSITY * speed_sqrd * DRAG_COEFF * AREA
    drag_x = drag * math.cos(angle)
    drag_y = -drag * math.sin(angle)
    return drag_x, drag_y

def updatePosition(pos, vel):
    pos_x = pos[0] + vel[0]
    pos_y = pos[1] + vel[1]
    return pos_x, pos_y

def updateVelocity(vel, acc):
    vel_x = vel[0] + acc[0]
    vel_y = vel[1] + acc[1]
    return vel_x, vel_y

def updateAcceleration(drag):
    acc_x = - drag[0] / BALL_MASS
    acc_y = (drag[1] + F_WEIGHT) / BALL_MASS
    return acc_x, acc_y

def updateForces():
    pass

""" define static parameters (don't change with time) """
BALL_MASS = 50 # units
BALL_RADIUS = 5 # pixels
GRAVITY = 0.5 # veritcal acceleration due to gravity
SEA_LEVEL = 500 # y = 100
F_WEIGHT = BALL_MASS * GRAVITY # weight acts veritically down

""" define physical constants for drag """
# fluid_density, speed, drag_coeff, cross_area, angle_radian
DENSITY = 0.005
DRAG_COEFF = 0.05
AREA = 3.1416 * BALL_RADIUS**2


""" define dynamic parameters (change with time) """
F_drag = [0, 0] # drag acts opposite to the 
position = [0, 0]
velocity = [0, 0]
acceleration = [0, GRAVITY]

""" set up launch conditions """
launch_position = [SIZE[0]/2, SEA_LEVEL - BALL_RADIUS]
speed = 10 # pixels per frame
launch_angle = 60
angle_radian = math.radians(launch_angle)
velocity[0] = speed * math.cos(angle_radian) # horizontal component
velocity[1] = -speed * math.sin(angle_radian) # veritcal component, flip y axis


""" simulation settings """
bounce = True # set to True if you want it to bounce off the invisble floor on y = 500
bounce_loss = [0.7, 0.8]
seconds = 8 # simulation duration

pg.time.delay(100)

while True and seconds > 0:
    
    position = list(position)
    velocity = list(velocity)
    acceleration = list(acceleration)

    seconds -= 1/fps # increment timer

    drawBackground()
    
    for event in pg.event.get():
        if (
            event.type == pg.QUIT
            or event.type == pg.KEYDOWN
            and event.key == pg.K_ESCAPE
        ):
            exit()
        
    # while not (event.type == pg.KEYDOWN and event.key == pg.K_SPACE): # don't launch until command
    #     continue
    # else:
    if bounce and (position[1] > (SEA_LEVEL - BALL_RADIUS)): # bounce off the ground
        """ reduce horizontal velocity due to friction """
        if velocity[0] > 0.1 or velocity[0] < -0.1: # keep moving horizontally if momentum big enough
            velocity[0] *= bounce_loss[0]
        else: # cease off bouncing completely if momentum too small
            position[0] = 0
            pass
        """ reduce vertical velocity due to kinetic energy loss """
        if velocity[1] > 0.1 or velocity[1] < -0.1: # keep bouncing up if momentum enough
            velocity[1] = - velocity[1] * bounce_loss[1]
        else: # stop bouncing if momentum too small
            position[1] = 0
        
    
    pg.draw.circle(screen, 'green', [position[0], position[1]], 6)
    
    position = updatePosition(position, velocity)
    velocity = updateVelocity(velocity, acceleration)
    
    speed_sqrd = velocity[0]**2 + velocity[1]**2
    angle_radian = -math.radians(math.atan2(velocity[1], velocity[0]))
    drag = getDrag(speed_sqrd, angle_radian)
    
    acceleration = updateAcceleration(drag)
    
    # print(int(position[0]), int(position[1]))
    # print(int(seconds), int(position[0]), int(position[1]), int(velocity[0]),
    #        int(velocity[1]), int(drag[0]), int(drag[1]), int(angle_radian))
    print(round(speed_sqrd,2), round(velocity[0], 2), round(velocity[1], 2))

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))