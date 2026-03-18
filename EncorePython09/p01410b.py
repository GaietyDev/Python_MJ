import turtle as t

def createCrosshair():
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.goto(200,0)

    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.goto(0,200)
    t.penup()
    t.goto(0,0)

createCrosshair()
dot_spawn_radius = int(input("Enter the spawn radius of the dots: "))
dot_spawn_radius = dot_spawn_radius * 200
