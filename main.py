from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

if __name__ == "__main__":
    x_win, y_win = 800, 600
    x_offset, y_offset = 30, 30
    cols, rows = 16, 12
    x_size = (x_win - x_offset - y_offset) / cols
    y_size = (y_win - x_offset - y_offset) / rows
    
    win = Window(x_win, y_win)
    maze = Maze(x_offset, y_offset, cols, rows, x_size, y_size, win)
    win.wait_for_close()
