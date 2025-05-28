from cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()


    def __create_cells(self):
        self.__cells = [[Cell(self.win) for y in range(self.num_rows)] for x in range(self.num_cols)]
        for j in range(self.num_cols):
            for i in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        cell = self.__cells[j][i]
        x1 = i * self.cell_size_x + self.x1
        y1 = j * self.cell_size_y + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        if self.win is None:
            return
        cell.draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.win is None:
            return
        self.win.redraw()


