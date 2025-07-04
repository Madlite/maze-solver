from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)


    def __create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self.__cells.append(col)
        for j in range(self.num_rows):
            for i in range(self.num_cols):
                self.__draw_cell(i, j)


    def __draw_cell(self, i, j):
        cell = self.__cells[i][j]
        x1 = i * self.cell_size_x + self.x1
        y1 = j * self.cell_size_y + self.y1
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        if self.win is None:
            return
        cell.draw(x1, y1, x2, y2)
        self.__animate()


    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()


    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0,0)
        self.__cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols-1, self.num_rows-1)


    def __break_walls_r(self, i, j):
        self.__cells[i][j].__visited = True

        while True:
            not_visited = []
            neighbors = [
                self.__cells[i][j-1], # top
                self.__cells[i][j+1], # bot
                self.__cells[i-1][j], # left
                self.__cells[i+1][j]  # right
            ]

            for neighbor in neighbors:
                if not neighbor.__visited:
                    not_visited.append(neighbor.x,neighbor.y)



