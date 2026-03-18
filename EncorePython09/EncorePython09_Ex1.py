from turtle import Turtle

t = Turtle()
user_input = input("Enter the x, y value of the starting position: ")
while user_input != 'quit':
    cordinate_list = user_input.split(',')
    user_x = int(cordinate_list[0])
    user_y = int(cordinate_list[1])

    t.penup()
    t.goto(user_x, 100+user_y)
    t.pendown()

    t.width(2)
    t.pencolor('red')
    t.setheading(270)
    t.forward(100)

    t.width(4)
    t.pencolor('blue')
    t.left(90)
    t.forward(100)

    t.width(6)
    t.pencolor('green')
    t.goto(user_x, 100+user_y)

    t.penup()
    user_input = input("Enter the x, y value of the starting position: ")
print("You have quit the program")
