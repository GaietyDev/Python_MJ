'''
Python 30, Exercise 01b

A Python program that uses Tkinter to create a program that displays three frames.
The three frames are displayed in one row.

The background of each frame is of a randomly picked color from a set of 10.
The set of 10 colors are the colors used to code resistor values:
'black', 'saddle brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'white'

The three frames are colored using three random selections from this set of colors.

The three frames are displayed and the user is asked what resistance value these represent.

The process is repeated and the game ends when the user gets NUMQ in a row correctly.

J. M. Hinckley
2025
'''

from tkinter import *
from tkinter import ttk
from random import *

NUMQ = 10  # number of questions needed to get right in a row


# Form a new question.
# clear the input entry box
# randomly pick three colors
# calculate the value of the corresponding resistance
# Draw the colored bands
def newQuestion():
    global R
    # Clear anything out of the Entry box
    # ADD YOUR CODE HERE: 9
    
    d1 = 0
    while d1 == 0: # first digit is not zero
        d1 = randint(0,len(colors)-1)   # first digit
    d2 = randint(0,len(colors)-1)       # second digit
    d3 = 10
    while d3 > 6: # don't go above megohm multiplier
        d3 = randint(0,len(colors)-1)   # third digit
    R = (d1 * 10 + d2)*(10**d3)         # resistance value
    drawPattern(colors[d1], colors[d2], colors[d3])



# Draw a pattern of 3 color bands representing resistor bands
# Parameters c1, c2, c3 are three color names (strings)
# Draw a frame with each specified color
def drawPattern(c1, c2, c3):
    # REMOVE pass AFTER YOU ADD YOUR OWN CODE: 1
    pass

    # draw first band in color c1, column=1, row=1
    # ADD YOUR CODE HERE: 2

    # draw second band in color c2, column=2, row=1
    # ADD YOUR CODE HERE: 3

    # draw third band in color c3, column=3, row=1
    # ADD YOUR CODE HERE: 4



# Event handler for button press.
# compares the value entered by the user (rvalue) to the value
# represented by the color bands (R)
# If they match, count is incremented.
# If they don't match, count is set to zero.
# If count reaches NUMQ, state that game is done and disable the button.
def compare(*args):
    global count
    try:
        userValue = int(rvalue.get())
        if userValue == R:
            count += 1
            if count >= NUMQ:
                s = "{0} Correct & Done!".format(count)
                response.set(s)
                b.state(['disabled'])
            else:
                s = "{0} Correct".format(count)
                response.set(s)
                newQuestion()

        else:
            s = "No, R = {0} ohms".format(R)
            response.set(s)
            count = 0
            newQuestion()
            
    except ValueError:
        pass




# colors appearing on resistor bands
colors = ['black', 'saddle brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'gray', 'white']

# Instantiate a Tk object
root = Tk()

# Set the title of the window
root.title("Resistor colors")

# Create a frame and configure the columns
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame1 = ttk.Frame(mainframe, width=100, height=100, borderwidth=0, relief='sunken')
frame1.grid(column=1, row=1)

s=ttk.Style()
s.configure('A.TFrame', background='red', borderwidth=5, relief='raised')
frame2 = ttk.Frame(mainframe, width=100, height=100, style='A.TFrame')
frame2.grid(column=2, row=1)

t=ttk.Style()
t.configure('B.TFrame', background='green', borderwidth=5, relief='raised')
frame3 = ttk.Frame(mainframe, width=100, height=100, style='B.TFrame')
frame3.grid(column=1, row=2)

u=ttk.Style()
u.configure('C.TFrame', background='blue', borderwidth=5, relief='raised')
frame4 = ttk.Frame(mainframe, width=100, height=100, style='C.TFrame')
frame4.grid(column=2, row=2)

 

# Create a Label "What is R?", column=1, row=2
# ADD YOUR CODE HERE: 5

# Create an Entry box to input user's answer, textvariable=rvalue, column=2, row=2
# ADD YOUR CODE HERE: 6

# Create a Button to run compare function, text="Check", command=compare, column=3, row=2
# ADD YOUR CODE HERE: 7

# Create a Label to display the response, textvariable=response, column=1, row=3
# ADD YOUR CODE HERE: 8

# Initialize the count to zero
count = 0

# Bind the Enter key to running the compare funnction
# ADD YOUR CODE HERE: 10

# Set the focus to the entry box widget
# ADD YOUR CODE HERE: 11


# Start the game by asking a new question
newQuestion()            

# Run the event loop
root.mainloop()


