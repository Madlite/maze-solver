from graphics import Window, Line, Point
from cell import Cell

if __name__ == "__main__":
    win = Window(800, 600)
    c1 = Cell(win)
    c1.draw(50,50,80,80)
    win.wait_for_close()
