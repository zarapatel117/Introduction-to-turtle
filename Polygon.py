import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(350,450)
polygon=turtle.Turtle()

num_sides=6
side=80
angle=360.00/num_sides
for i in range(num_sides):
    polygon.forward(side)
    polygon. right(angle)