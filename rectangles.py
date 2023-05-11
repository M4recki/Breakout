from turtle import Turtle


class Rectangles(Turtle):
    def __init__(self):
        super().__init__()
        self.rectangles_list = []
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.create_rectangles(5, 5, 6)

    def create_rectangles(self, rows, columns, size):
        colors = ["purple", "orange", "yellow", "green", "blue"]
        x_start = -270
        y_start = 260

        # Set initial position of turtle
        self.setpos(x_start, y_start)

        # Create rows and columns of rectangles
        for i in range(rows):
            for j in range(columns):
                self.color(colors[i])
                self.shapesize(stretch_wid=1, stretch_len=size)
                self.stamp()
                self.rectangles_list.append(self)

                if j != columns - 1:
                    self.forward(size * 2)
                    self.setx(self.xcor() + size * 10 + 10 * size)

            # Move the turtle back to the left edge and down by y_gap pixels
            self.setpos(x_start,  y_start - (i+1)*size*5)
