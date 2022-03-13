'''
DrawRandom.py

@author: alyssa ting
'''

import turtle, BoundingBox, TurtleShapes, random

def drawEverywhere(turt, func):

    """
    This function takes input from the user to determine how many shapes it
    draws, then draws that number of shapes in random sizes and at random
    locations within the window.
    """

    number = int(input("How many do you want to draw? "))

    for i in range(number):
        size = random.randrange(20, 90)
        xrand = random.randrange(-400, 350)
        yrand = random.randrange(-150, 100)

        turt.up()
        turt.setposition(xrand, yrand)
        turt.down()

        func(turt,size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()

    eturt = turtle.Turtle()

    type = int(input("Input 0 for drawOneShape, 1 for drawOneHouse "))
    if type == 0:
        func = TurtleShapes.drawOneShape
    else:
        func = TurtleShapes.drawOneHouse

    drawEverywhere(eturt, func)

    win.exitonclick()
    