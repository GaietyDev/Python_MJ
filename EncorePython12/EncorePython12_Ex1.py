import turtle as t

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        t.pencolor(self.color)
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.goto(200,0)

class Rectangle(Shape):
    def __init__(self, color, corner, width, height):
        self.color = color
        self.corner = corner
        self.width = width
        self.height = height
        
    def drawRectangle(self):
        for sides in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)
        

    def draw(self):
        x, y = self.corner
        t.pencolor(self.color)
        t.penup()
        t.goto(x,y)
        t.pendown()
        count = 0
        for col in range(3):
            for row in range(3):
                t.goto(x + self.width*row, y - self.height*col)
                self.drawRectangle()
            t.penup()
            t.goto(x,y)
            t.pendown()
            
        for yCenter in range(3):
            for xCenter in range(3):
                count += 1
                t.penup()
                t.goto(x+self.width*xCenter + self.width/2 , y - self.height*yCenter - self.height/2)
                t.pendown()
                t.write(count)
                t.penup()
                
        t.penup()

class Triangle(Shape):
    def __init__(self, color, x1, y1, x2, y2, x3, y3):
        self.color = color
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def drawTriangle(self, x1,y1, x2,y2, x3,y3, count, upside_down, y_half):
        t.penup()
        t.goto(x1,y1)
        t.pendown()
        t.goto(x2,y2)
        t.goto(x3,y3)
        t.penup()
        
        if upside_down:
            t.goto(x3,y3+y_half)
            t.pendown()
            t.write(count)
            t.penup()
        else:
            t.goto(x3,y3-y_half) 
            t.pendown()
            t.write(count)
            t.penup()

        t.goto(x3,y3)
        t.pendown()
        t.goto(x1,y1)
    
    def draw(self):
        shape_amount = 5
        count = 0
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2
        x3 = self.x3
        y3 = self.y3
        t.pencolor(self.color)
        y_half = -(y3/2)
        for col in range(3):
            shape_num = shape_amount-2*col
            upside_down = True
            #print(shape_num)
            #print()
            for row in range(shape_num):
                x_horizontal = x3*row
                x_vertical = x3*col
                count += 1
                if upside_down:
                    y_vertical = -y3*col
                    self.drawTriangle(x1+x_horizontal+x_vertical, y1-y_vertical,
                                      x2+x_horizontal+x_vertical, y2-y_vertical,
                                      x3+x_horizontal+x_vertical, y3-y_vertical,
                                      count, upside_down, y_half)
                    #print("%d: %d,%d %s" % (row, x3+x_horizontal+x_vertical, y3-y_vertical, upside_down))
                    upside_down = False
                else:
                    y_vertical = -y3*(col+1)
                    self.drawTriangle(x1+x_horizontal+x_vertical, y1-y_vertical,
                                       x2+x_horizontal+x_vertical, y2-y_vertical,
                                       x3+x_horizontal+x_vertical, y3+y_vertical-y_vertical*col,
                                       count, upside_down, y_half)
                    #print("%d: %d,%d %s" % (row,x3+x_horizontal+x_vertical, y3+y_vertical-y_vertical*col, upside_down))
                    upside_down = True

class Circle(Shape):
    def __init_(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self):
        x = self.x
        y = self.y
        radius = self.radius
        t.pencolor(self.color)
        t.penup()
        
test = Circle('green', 0,0, 80)
test.draw()
