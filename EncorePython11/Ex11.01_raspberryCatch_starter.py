import pygame
from pygame.locals import *
from sys import exit
import random

# parameter definitions
score = 0
screen_width = 600
screen_height = 400
spoon_x = 300
spoon_y = screen_height - 100

#-------------------------------------------------

# Template defining a raspberry

class Raspberry:
    def __init__(self):         # initialization of a Raspberry
         self.x: random horizontal pos.
         self.y: start at top
         self.dy: random step size, between 1 and 5

    def update(self):           # update position each cycle of game loop
        $# move down a bit
        $# is rasp past the spoon?
            $# yes, go back to top
            $# random horizontal pos.
        $# random lateral offset (+/- 5 jiggle)
        $# close to left side?
            $# hard limit at 10 on left side
        $# close to right side?
            $# hard limit on right, too.
        screen.blit(raspberry_image, (self.x, self.y)) # update pygame with new location
                                                    

    def is_caught(self):        # is the raspberry in the spoon?
        $# a: True if raspberry is at or below spoon.
        $# b: True if raspberry is at or right of spoon.
        $# c: True if raspberry is at or left of sp. bowl
        return a and b and c

#-------------------------------------------------

# Main program        
        
clock = pygame.time.Clock()
rasps = [Raspberry(),Raspberry(),Raspberry()] # instantiate 3 Raspberries

pygame.init()   # initialize pygame module

# Set up the game
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Raspberry Catching')
spoon = pygame.image.load('spoon.jpg').convert()
raspberry_image = pygame.image.load('raspberry.jpg').convert()

#--------------------------------------------

# some game loop functions

def update_spoon():
    global spoon_x
    global spoon_y
    spoon_x, _ = pygame.mouse.get_pos() # get location of cursor, ignore y
    screen.blit(spoon,(spoon_x, spoon_y))   # update game object

def check_for_catch():
    global score
    $# loop over each raspberry
        $# is the raspberry caught?
        $# increment score

def display(message):
    font = pygame.font.Font(None,36)
    text = font.render(message, 1, (10,10,10))
    screen.blit(text, (0,0))    # update game object

#--------------------------------------------

# The game loop.

while True:

    # gracefully end by pressing "X" in window corner
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))  # setting background color (white)

    # update each raspberry
    $# loop over raspberries
        $# run Raspberry update function

    $# move spoon: run spoon update function
    $# did catch one?
    $# show new score
    pygame.display.update()         # redraw display with updated game objects
    clock.tick(30)                  # for every second 30 frames shown





    








    
