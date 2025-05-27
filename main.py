from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

if __name__ == "__main__":
    win = Window(800, 600)
    m = Maze(30, 30, 10, 10, 30, 30, win)
    win.wait_for_close()
