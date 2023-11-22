import turtle

# sets pen colour to blue
turtle.pencolor("blue")

# lifts the pen to start drawing
turtle.penup()
#sets position of pen at the specified coordinates
turtle.setposition(-45, 100)

#places the pen down to start drawing
turtle.pendown()

#loop to draw an octagon
for i in range(8):
    turtle.forward(80) #sides are 80 units long
    turtle.right(45) #each vertex is 45 degrees

#draw a spiral within the octagon
distance = 0.2
angle = 40
turtle.pencolor("red")
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()

#loop to draw the spiral
for i in range(100):
    turtle.forward(distance)
    turtle.left(angle)
    distance += 0.5
turtle.hideturtle() #makes turtle invisible
turtle.exitonclick() #exits program when user clicks on mouse button
