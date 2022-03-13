'''
TurtleShapes.py

@author: alyssa ting
'''

import turtle, BoundingBox

def drawOneShape(turt, size):
    """
    This function uses a turtle to draw a square of parameter size. It takes
    two parameters, a turtle and a size.
    """
    for i in range (4):
        turt.forward(size)
        turt.right(90)

def drawOneHouse(turt,size):
    """
    This function draws a multicolored house with a roof and a door, with a pen
    size of 7. It takes two parameters, a turtle and a size.
    """
    turt.pensize(7)
    turt.fillcolor('turquoise')
    turt.begin_fill()
    for color in ["dark blue", "blue", "light blue", "turquoise"]:
        turt.color(color)
        turt.right(90)
        turt.forward(size)
    turt.end_fill()

    turt.fillcolor('red')
    turt.begin_fill()

    for anotherColor in ["orange", "red"]:
        turt.color(anotherColor)
        turt.left(120)
        turt.forward(size)
    turt.end_fill()

    turt.up()
    turt.left(30)
    turt.forward(size)
    turt.left(90)

    turt.down()
    turt.fillcolor("brown")
    turt.begin_fill()
    turt.forward(size/3)
    turt.left(90)
    turt.forward(size/3)
    turt.right(90)
    turt.forward(size/4)
    turt.right(90)
    turt.forward(size/3)
    turt.end_fill()
    turt.left(90)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    ## CALL FUNCTIONS HERE
    t = turtle.Turtle()
    t.up()
    t.setposition(-100,100)
    t.down()
    drawOneShape(t,50)

    hturt = turtle.Turtle()
    hturt.up()
    hturt.setposition(150,50)
    hturt.down()
    drawOneHouse(hturt,100)

    win.exitonclick()
    