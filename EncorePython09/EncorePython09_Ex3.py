import turtle as t

colors = ['red','green','blue',
          'orange','yellow','purple',
          'indigo','brown','white',
          'cyan', 'dark blue','maroon']
degree = 0

sides = int(input("Enter the number of sides between 2 and 12: "))
while sides < 2 or sides > 12:
    print("|! INPUT MUST BE BETWEEN 2 AND 12 !|")
    print()
    sides = int(input("Enter the number of sides between 2 and 12: "))

t.speed(0)
t.Screen().bgcolor('black')

t.penup()
t.goto(0,0)
t.pendown()

for x in range(360):
    t.width(1 + x/360)
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(360/sides + 0.5)
