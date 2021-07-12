#Python programming to draw shapes in turtle programming
import turtle

t = turtle.Turtle()
t.color("red", "blue")
pen = turtle.Turtle()
SideCount = int(input("How many sides? (Only up to 10 sides) "))

if SideCount == 3:
    Angle = 120
    pen.write("Triangle", font=("Calibri", 15, "bold"))

if SideCount == 4:
    Angle = 90
    pen.write("Square", font=("Calibri", 15, "bold"))

if SideCount == 5:
    Angle = 72
    pen.write("Pentagon", font=("Calibri", 15, "bold"))

elif SideCount == 6:
    Angle = 60
    pen.write("Hexagon", font=("Calibri", 15, "bold"))
    
elif SideCount == 7:
    Angle = 51.42
    pen.write("Heptagon", font=("Calibri", 15, "bold"))

elif SideCount == 8:
    Angle = 45
    pen.write("Octagon", font=("Calibri", 15, "bold"))

elif SideCount == 9:
    Angle = 40
    pen.write("Nanogon", font=("Calibri", 15, "bold"))

elif SideCount == 10:
    Angle = 36
    pen.write("Decagon", font=("Calibri", 15, "bold"))

turtle.pencolor("red")
t.width(5)
for i in range(SideCount):
    t.forward(50) #Assuming the side of a pentagon is 100 units
    t.right(Angle) #Turning the turtle by 72 degree
turtle.done()