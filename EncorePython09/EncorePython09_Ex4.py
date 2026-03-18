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
