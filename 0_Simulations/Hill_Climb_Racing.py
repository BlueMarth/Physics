import pygame as pg
from pygame.locals import *
import math

SIZE = (960, 600)
screen = pg.display.set_mode(SIZE)

clock = pg.time.Clock()
fps = 60


""" define static parameters (don't change with time) """
CAR_MASS = 100 # units
CAR_SIZE = (200, 50) # pixels
GRAVITY = 0.6 # veritcal acceleration due to gravity
ROAD_LEVEL = 500 # y = 100
F_WEIGHT = CAR_MASS * GRAVITY # weight acts veritically down

""" define physical constants for drag """
# fluid_density, speed, drag_coeff, cross_area, angle_radian
DENSITY = 0.005
DRAG_COEFF = 0.1
AREA = 50

""" define dynamic parameters (change with time) """
pos_x, pos_y = 0, 0
vel_x, vel_y = 0, 0
acc_x, acc_y = 0, 0

""" set up initial conditions """
pos_x = SIZE[0]//2 - 350
pos_y = ROAD_LEVEL - CAR_SIZE[1]

""" simulation settings """


""" User Interaction """

def getInputs():
    for event in pg.event.get():
        if (event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            exit()

    

""" Game Logic """

def initiate_Car():
    pass

def drive_Car():
    pass

""" Physics Engine """
def updateForces():
    pass

def integrator():
    pass


""" Render """
def renderGraphics(x, y):
    screen.fill('black')
    pg.draw.line(screen, 'red', [0, ROAD_LEVEL], [SIZE[0], ROAD_LEVEL], 1)
    
    pg.draw.rect(screen, "green", [x, y, CAR_SIZE[0], CAR_SIZE[1]])
    
    pg.display.update()

while True:
    
    getInputs()
    renderGraphics()
    
    clock.tick(fps)
    pg.display.set_caption("fps: " + str(clock.get_fps()))