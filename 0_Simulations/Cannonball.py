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
    acc_x = 0 #- drag[0] / BALL_MASS
    acc_y = F_WEIGHT / BALL_MASS # (drag[1] + F_WEIGHT) / BALL_MASS
    return acc_x, acc_y


""" define static parameters (don't change with time) """
BALL_MASS = 100 # units
BALL_RADIUS = 6 # pixels
GRAVITY = 0.6 # veritcal acceleration due to gravity
SEA_LEVEL = 500 # y = 100
F_WEIGHT = BALL_MASS * GRAVITY # weight acts veritically down
MOMENTUM_LIMIT = BALL_MASS

""" define physical constants for drag """
# fluid_density, speed, drag_coeff, cross_area, angle_radian
DENSITY = 0.005
DRAG_COEFF = 0.1
AREA = math.pi * BALL_RADIUS**2

""" define dynamic parameters (change with time) """
F_drag = [0, 0] # drag acts opposite to the 
position = [0, 0]
velocity = [0, 0]
acceleration = [0, GRAVITY]

""" set up launch conditions """
position = [SIZE[0] / 2 - 350, SEA_LEVEL - BALL_RADIUS]
speed = 10 # pixels per frame
launch_angle = -75
angle_radian = math.radians(launch_angle)
velocity[0] = speed * math.cos(angle_radian) # horizontal component
velocity[1] = speed * math.sin(angle_radian) # veritcal component, flip y axis

""" simulation settings """
bounce = True # set to True if you want it to bounce off the invisble floor on y = 500
bounce_loss = [0.85, 0.75] # changing y-loss may cause ever-bouncing glitch
seconds = 12 # simulation duration
does_bounce = "Yes"

pg.time.delay(100)

while True and seconds > 0:
    drawBackground()
    
    

    seconds -= 1/fps # increment timer

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
    position = updatePosition(position, velocity)
    velocity = updateVelocity(velocity, acceleration)
    
    speed_sqrd = velocity[0]**2 + velocity[1]**2
    momentum = BALL_MASS * math.sqrt(speed_sqrd)

    angle_radian = math.radians(math.atan2(velocity[1], velocity[0]))
    drag = getDrag(speed_sqrd, angle_radian)
    
    acceleration = updateAcceleration(drag)  

    position = list(position)
    velocity = list(velocity)
    acceleration = list(acceleration)

    not_enough_momentum = (SEA_LEVEL - 1.5 * BALL_RADIUS < position[1] <= SEA_LEVEL - 0.5 * BALL_RADIUS) and (-10 < momentum < 10)
    if not_enough_momentum: # stop bouncing if not enough momentum
            velocity = [0, 0]
            position[1] = SEA_LEVEL - BALL_RADIUS
            does_bounce = "No"
    elif bounce and (position[1] > (SEA_LEVEL - BALL_RADIUS)) and velocity[1] > 0:
        velocity[0] *= bounce_loss[0]
        velocity[1] *= -bounce_loss[1]
        does_bounce = "Yes"

    pg.draw.circle(screen, 'green', [position[0], position[1]], BALL_RADIUS)
    
    print('Position', round(position[1], 2),
          'velocity_y', round(velocity[1], 2),
          'not enough momentum', not_enough_momentum,
          'bouncing', does_bounce)

    pg.display.update()
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))