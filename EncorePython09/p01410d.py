import turtle as t
import random
import math

def createCrosshair():
    t.penup()
    t.speed(0)
    t.goto(-200,0)
    t.pendown()
    t.goto(200,0)

    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.goto(0,200)
    t.penup()
    t.goto(0,0)

def createDot(x, y, radius):
    t.goto(x, y)
    t.dot(radius, "yellow")
    t.goto(0,0)

def shootRay(angle, distance):
    angle = float(angle)

    t.pendown()
    t.left(angle)
    t.forward(distance)
    t.penup()
    t.goto(0,0)
    t.right(angle)
    
createCrosshair()

dot_radius_world = float(input("Enter the radius of the targets: "))
dot_radius_view = dot_radius_world * 200

while True:
    dot_x_world = random.uniform(-2.0, 2.0)
    dot_y_world = random.uniform(-2.0, 2.0)

    origin_distance_squared = pow(dot_x_world, 2) + pow(dot_y_world, 2)
    origin_distance_world = math.sqrt(origin_distance_squared)
        
    if origin_distance_world < (dot_radius_world * 1.25):
        continue

    dot_x_view = dot_x_world * 200
    dot_y_view = dot_y_world * 200
    origin_distance_view =  origin_distance_world * 200

    createDot(dot_x_view, dot_y_view, dot_radius_view)

    user_input = input("Enter the trajectory angle(degrees) or 'x' to quit: ")
    if user_input == 'x':
        break
    
    shootRay(user_input, origin_distance_view)
    
