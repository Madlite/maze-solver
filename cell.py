from graphics import Line, Point

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__visited = False 
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win is None:
            return

        # LEFT
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        # RIGHT
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        # TOP
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

        # BOTTOM
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line)
        else:
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        x_diff = (self.__x2 - self.__x1) / 2
        y_diff = (self.__y2 - self.__y1) / 2
        p1_middle = Point(self.__x1 + x_diff, self.__y1 + y_diff)

        x_diff = (to_cell.__x2 - to_cell.__x1) / 2
        y_diff = (to_cell.__y2 - to_cell.__y1) / 2
        p2_middle = Point(to_cell.__x1 + x_diff, to_cell.__y1 + y_diff)

        line = Line(p1_middle, p2_middle)
        if self.__win is None:
            return
        self.__win.draw_line(line)