from turtle import Turtle


class Rectangles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.rectangles_list = []

    def create_rectangles(self, rows, columns, size):
        colors = ["purple", "orange", "yellow", "green", "blue"]
        x_start = -275
        y_start = 260

        # Set initial position of turtle
        self.setpos(x_start, y_start)

        # Add more gap between each of rectangles
        gap = size * 8

        # Create rows and columns of rectangles
        for i in range(rows):
            for j in range(columns):
                self.color(colors[i])
                self.shapesize(stretch_wid=1 , stretch_len=size)
                self.stamp()
                self.forward(size*10)
                self.rectangles_list.append(self)
                if i == rows - 1 and j == columns - 2:
                    break
            else:
                self.setpos(x_start, y_start - (i+1)*size*5)
                continue
            break

