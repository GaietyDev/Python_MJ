import threading
import turtle
import time

# --- Threading Class ---
class SpiralThread(threading.Thread):
    def __init__(self, params_dict):
        # Initialize the base threading class
        super().__init__(name=params_dict['name'])
        
        # Unpack the dictionary into instance variables
        self.x = params_dict['x']
        self.y = params_dict['y']
        self.color = params_dict['color']
        self.speed_factor = params_dict['speed']

    def run(self):
        # Instantiate a unique turtle object for this thread
        # (Using RawTurtle allows it to play nicer with multithreading)
        t = turtle.RawTurtle(turtle.Screen())
        t.speed(0) # Set animation speed to fastest so it draws smoothly
        
        # Move the turtle to its unique starting position without drawing
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        
        # Set the spiral color
        t.color(self.color)
        
        # Draw the spiral
        # A slower "speed factor" results in a tighter, smaller spiral
        for i in range(1000):
            # The step size increases slightly, and scales based on the speed factor
            step = (i * 0.01) * self.speed_factor
            t.forward(step)
            t.left(4)  # Tight angle to create the spiral effect
            
        # Lift the pen up upon completion
        t.penup()


# --- Main Function ---
def main():
    # Setup the shared screen configuration
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")

    # Define lists of parameters for the 4 spirals
    x_coords = [-200, 200, -200, 200]
    y_coords = [200, 200, -200, -200]
    colors = ["red", "blue", "green", "purple"]
    speeds = [0.5, 1.0, 1.5, 2.0] # Controls relative size (slower = smaller)

    # Empty list to hold dictionaries for each thread
    thread_parameters = []

    # First Loop: Populate the configuration dictionaries
    for i in range(4):
        thread_name = f"SpiralThread-{i}"
        
        # Create a dictionary containing the parameters for this specific spiral
        params = {
            'name': thread_name,
            'x': x_coords[i],
            'y': y_coords[i],
            'color': colors[i],
            'speed': speeds[i]
        }
        
        # Append to the main list
        thread_parameters.append(params)

    # List to keep track of active thread objects
    active_threads = []

    # Second Loop: Instantiate and start the threads
    for params in thread_parameters:
        # Instantiate the custom threading object, passing the dictionary
        t_obj = SpiralThread(params)
        active_threads.append(t_obj)
        
        # Start the thread execution
        t_obj.start()
        # Small sleep delay to prevent tkinter from freezing during initialization
        time.sleep(0.2) 

    # Keep the window open until clicked after threads finish
    screen.exitonclick()

if __name__ == "__main__":
    main()
# Modified AI Generated Code 
