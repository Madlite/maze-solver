from graphics import Window, Line, Point

if __name__ == "__main__":
    win = Window(800, 600)
    l1 = Line(Point(100, 100), Point(500, 500))
    win.draw_line(l1, "red")
    win.wait_for_close()
