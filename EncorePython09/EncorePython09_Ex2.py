from turtle import Turtle

t = Turtle()

def drawSquare(x, y, l, t):

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(l)

    t.right(90)
    t.forward(l)

    t.right(90)
    t.forward(l)

    t.right(90)
    t.forward(l)

    t.penup()
# End of Function

square_list = [(200,100,50),
               (100,300,100),
               (300,50,200)]
for i in range(3):

    x = square_list[i][0]
    y = square_list[i][1]
    l = square_list[i][2]
    drawSquare(x,y,l,t)
