from graphics import *
import math

win = GraphWin("DDA Line Drawing Algorithm", 600, 600)

def drawDDALine(px1,py1,px2,py2):
	x1 = px1
	x2 = px2
	y1 = py1
	y2 = py2

	dx = x2-x1
	dy = y2-y1
	steps = 0
	xInc = 0.0
	yInc = 0.0

	x = x1
	y = y1

	if ( abs(dx) > abs(dy) ):
		steps = abs(dx)
	else:
		steps = abs(dy)

	stepsFloat = float(steps)

	xInc = dx/stepsFloat
	yInc = dy/stepsFloat



	c = Circle(Point(x,y),1)
	c.draw(win)

	for a in range(steps):

		x+=xInc
		y+=yInc


		c = Circle(Point(x,y),1)
		c.draw(win)





def main():
    

    drawDDALine(30,30,430,70)
    drawDDALine(30,40,430,370)

    drawDDALine(430,370,60,30)
    drawDDALine(430,370,360,30)

    drawDDALine(30,370,360,30)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()