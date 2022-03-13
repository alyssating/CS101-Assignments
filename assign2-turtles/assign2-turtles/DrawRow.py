'''
DrawRow.py

@author: alyssa ting
'''

import turtle, BoundingBox, TurtleShapes, random

def drawRowsOfRows(turt, func):
    """
    This function draws ten rows of houses. The houses in a given row
    all have the same size and y-coordinate, and the size used in a given row
    is different from the size used in other rows.
    """
    s = 20
    for y in range(200,-200,-40):
        s += 10
        for x in range (-200,200,40):
            turt.up()
            turt.setposition(x,y)
            turt.down()
            func(turt,s)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    rturt = turtle.Turtle()

    drawRowsOfRows(rturt,TurtleShapes.drawOneHouse)
    
    win.exitonclick()
    