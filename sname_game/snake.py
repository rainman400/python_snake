from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        position = 0
        for _ in range(0, 3):
            self.add_segment((position, 0))
            position -= 20

    def add_segment(self, position):
        add_segment = Turtle(shape="square")
        add_segment.color("white")
        add_segment.penup()
        add_segment.goto(position)
        self.snake_body.append(add_segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[seg_num].goto(self.snake_body[seg_num - 1].xcor(), self.snake_body[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
