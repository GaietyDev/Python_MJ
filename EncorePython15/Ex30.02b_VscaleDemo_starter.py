'''
Python 30, Exercise 02b (starter)

A Python program that uses Tkinter to create a
program that exhibits a vertical Scale (slider) widget
controlling a integer value.

J. M. Hinckley
2025
'''

from tkinter import *
from tkinter import ttk


# get the current value of the slider as an integer
def get_slider_value():
    return '{: d}'.format(current_value.get())


# event handler for slider position changed
def slider_changed(event):
    value_label.configure(text=get_slider_value())


# create and configure the root window
root = Tk()
root.geometry('200x300')
root.resizable(False, False)
root.title('Vertical Slider Demo')


#-----------------------------------------
    
# create the label to display "Slider:"
slider_label = ttk.Label(
    root,
    text='Slider:'
)


# locate the label, column=0, row=0, pad with 10 pixels in x and in y
# ADD YOUR CODE HERE: 1


#----------------------------------------- 

# define variable for the slider's current value
current_value = IntVar()

# create the slider, ranging from 0 to 100, oriented vertically, having a
# length of 200, command=slider_changed, variable=current_value
# ADD YOUR CODE HERE: 2


# locate the slider; spans rows 1 and 2, locate in column=0, row=1,
# pad 10 pixels in x and y
# ADD YOUR CODE HERE: 3

#-----------------------------------------
    
# create a label to display "Current Value:"
current_value_label = ttk.Label(
    root,
    text='Current Value:'
)

# locate the label, column=1, row=1, pad with 10 pixels in x and in y
# ADD YOUR CODE HERE: 4

#-----------------------------------------
    
# create a dynamic label to display the value of the slider
# text=get_slider_value()
# ADD YOUR CODE HERE: 5

# locate the dynamic label, column=1, row=2, pad with 10 pixels in x and in y
# ADD YOUR CODE HERE: 6

#-----------------------------------------
    
# start the event loop
root.mainloop()
