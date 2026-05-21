import threading
import turtle

# Thread class for drawing a spiral
class SpiralThread(threading.Thread):
    def __init__(self, params):
        super().__init__(name=params["name"])

        # Unpack dictionary values into instance variables
        self.t = params["turtle"]
        self.x = params["x"]
        self.y = params["y"]
        self.color = params["color"]
        self.speed = params["speed"]

    def run(self):
        # Set turtle properties
        self.t.color(self.color)
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()

        # Draw spiral
        for i in range(1000):
            self.t.forward(i * 0.02 * self.speed)
            self.t.left(91)

        # Finish drawing
        self.t.penup()


def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Empty list of dictionaries
    spiral_data = []

    # Lists of parameters
    x_values = [-200, 200, -200, 200]
    y_values = [200, 200, -200, -200]
    colors = ["red", "blue", "green", "yellow"]
    speeds = [0.5, 1, 1.5, 2]

    # Create dictionaries for each spiral
    for i in range(4):
        t = turtle.Turtle()

        params = {
            "name": f"SpiralThread-{i+1}",
            "turtle": t,
            "x": x_values[i],
            "y": y_values[i],
            "color": colors[i],
            "speed": speeds[i]
        }

        spiral_data.append(params)

    # Create and start threads
    threads = []

    for params in spiral_data:
        thread = SpiralThread(params)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    turtle.done()


if __name__ == "__main__":
    main()
# AI Generated Code
