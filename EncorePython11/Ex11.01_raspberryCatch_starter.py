import pygame
from pygame.locals import *
from sys import exit
import random

# parameter definitions
score = 0
screen_width = int(input("Enter how wide the screen should be: "))
screen_height = int(input("Enter how tall the screen should be: "))
spoon_x = 300
spoon_y = screen_height - 100
input_fps = int(input("Enter the FPS: "))
colors = {'white':(255,255,255),
          'red':(255,0,0),
          'orange':(255,201,14),
          'yellow':(255,255,0),
          'green':(0,255,0),
          'cyan':(0,255,255),
          'blue':(0,0,255),
          'violet':(68,0,255),
          'magenta':(255,0,255)}

# input validation for background color
while True:
    input_color = input("Enter the background color: ")
    input_color = input_color.lower()
    if input_color in colors.keys():
        break
    else:
        print("|! INVALID COLOR !|")
        print("list of valid colors:")
        for key in colors.keys():
           print(key)
        print()

#-------------------------------------------------

# Template defining a raspberry

class Raspberry:
    def __init__(self):         # initialization of a Raspberry
         self.x = random.randint(10, screen_width)
         self.y = 0
         self.dy = random.randint(1,5)

    def update(self):           # update position each cycle of game loop
        self.y += self. dy
        if self.y > spoon_y:
            self.y = 0
            self.x = random.randint(10, screen_width)
        self.x += random.randint(-5, 5) # random lateral offset (+/- 5 jiggle)
        if self.x < 10: # close to left side?
            self.x = 10 # hard limit at 10 on left side
        if self.x > screen_width - 20:  # close to right side?
            self.x > screen_width - 20 # hard limit on right, too.
        screen.blit(raspberry_image, (self.x, self.y)) # update pygame with new location
                                                    

    def is_caught(self):           # is the raspberry in the spoon?
        a = self.y >= spoon_y      # a: True if raspberry is at or below spoon.
        b = self.x >= spoon_x      # b: True if raspberry is at or right of spoon.
        c = self.x <= spoon_x + 50 # c: True if raspberry is at or left of sp. bowl
        return a and b and c

#-------------------------------------------------

# Main program        
        
clock = pygame.time.Clock()
rasps = [Raspberry()] # instantiate 1 raspberry

rasps_amount = int(input("Enter the amount of raspberrys in play: "))
for r in range(rasps_amount):
    raspberry = Raspberry()
    rasps.append(raspberry)

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
    for r in rasps:         # loop over each raspberry
        if r.is_caught():   # is the raspberry caught?
            score += 1      # increment score

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

    screen.fill(colors[input_color])  # setting background color (white)

    # update each raspberry
    for r in rasps:  # loop over raspberries
        r.update()   # run Raspberry update function

    update_spoon()    # move spoon: run spoon update function
    check_for_catch() # did catch one?
    display("Score: " + str(score)) # show new score
    pygame.display.update()         # redraw display with updated game objects
    clock.tick(input_fps)           # for every second 30 frames shown




    








    
