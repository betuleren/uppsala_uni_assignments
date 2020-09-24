import turtle


# Put the functions (jump, make_turtle, rectangle, tricolore and pentagram) in a Python file:

def jump(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def make_turtle(x, y):
    t = turtle.Turtle()
    jump(t, x, y)    # Use of the function defined above
    return t

def rectangle(x, y, width, height, color):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
def tricolore(x, y, h):
    w = h/2  #The width of the color field
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+2*w, y, w, h, 'red')

    
# Modify the pentagram function so that it takes a parameter for the fill color:

def pentagram(x, y, side, color):
    t = make_turtle(x, y)
    t.speed(0)
    t.hideturtle()
    t.setheading(270 - 36/2)
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()
    
    
# Write code that produces the figure:
    
# tricolore(10,10, 50)

#for i in [10,30,50,70,90]:
#    pentagram(i, 5, 20, "green")
#    pentagram(i, 85, 20, "green")
    
    
# clear the drawings:




def run():
    jump()
    make_turtle()
    rectangle()
    tricolore()
    pentagram()
    tricolore(10, 10, 50)

    for i in [10, 30, 50, 70, 90]:
        pentagram(i, 5, 20, "green")
        pentagram(i, 85, 20, "green")
    turtle.clearscreen()


if __name__ == "__main__":
    run()



