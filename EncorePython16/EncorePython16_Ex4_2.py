import threading
import turtle
import time
import queue

# YouTube video to help
# https://www.youtube.com/watch?v=Ir6wNTUWC74

# Create Queue object
q = queue.Queue()

# --- Threading Class ---
class SpiralThread(threading.Thread):
    def __init__(self, params_dict):
        # Initialize the base threading class
        super().__init__(name=params_dict['name'], args=(q,), daemon=True)
        
        # Unpack the dictionary into instance variables
        self.name = params_dict['name']
        self.x = params_dict['x']
        self.y = params_dict['y']
        self.color = params_dict['color']
        self.speed_factor = params_dict['speed']
        self.t = params_dict[self.name]
        self.lock = threading.Lock()
        self.loops = 0

    def run(self):
        global q,
        t = self.t
        t.speed(0) # Set animation speed to fastest so it draws smoothly
        
        # Move the turtle to its unique starting position without drawing
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        
        # Set the spiral color
        t.color(self.color)

        # Draw Spiral        
        # A slower "speed factor" results in a tighter, smaller spiral
        # The step size increases slightly, and scales based on the speed factor
        for i in range(10000):
            self.lock.acquire()
            step = (i*0.5) *self.speed_factor
            q.put(self.name)
            q.put(step)
            self.lock.release()
            time.sleep(1)
            #print("test " +f"{i}")
            #print(q.get())
     
        # Lift the pen up upon completion
        t.penup()

    


# --- Main Function ---
def main():
    global q, thread_done

    def drawSpiral():
        pass
    
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
        t = turtle.RawTurtle(turtle.Screen())
        
        # Create a dictionary containing the parameters for this specific spiral
        params = {
            'name': thread_name,
            'x': x_coords[i],
            'y': y_coords[i],
            'color': colors[i],
            'speed': speeds[i],
            thread_name : t
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
        t_obj.start()
    for thread in active_threads:
        thread.join()

    while thread_done != 4:
        time.sleep(0.01)
        threadName = q.get()
        step = q.get()
        t = active_threads[thread_name]
        print(t)
        t.forward(step)
        t.left(25)
    print("queue ended")
        
    # Keep the window open until clicked after threads finish
    screen.exitonclick()

main()
print("finished")
# Modified AI Generated Code 
