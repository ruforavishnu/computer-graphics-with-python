from graphics import *

def main():
    win = GraphWin("My Circle", 400, 400)
    c = Circle(Point(50,50), 10)
    c.draw(win)



    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()