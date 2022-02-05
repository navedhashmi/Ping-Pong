from turtle import Turtle


class PadA(Turtle):

    def __init__(self):
        super().__init__()
        self.LOCATION_A = []
        self.paddle_location = [(-380, 0), (-380, 25), (-380, 50), (-380, 75)]
        self.paddle_inventory = []
        self.paddle_inventory_up = []
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.pensize(4)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for x in range(1, 21):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)

    def paddle_a(self):
        for x in self.paddle_location:
            paddle = Turtle("square")
            paddle.color("white")
            paddle.shapesize(1.3)
            paddle.penup()
            paddle.goto(x)
            self.paddle_inventory.append(paddle)
        self.paddle_inventory_up = self.paddle_inventory[::-1]

    def move(self):
        for x in range(len(self.paddle_inventory) - 1, 0, -1):
            new_x = self.paddle_inventory[x - 1].xcor()
            new_y = self.paddle_inventory[x - 1].ycor()
            self.paddle_inventory[x].goto(new_x, new_y)
        self.paddle_inventory[0].fd(25)

    def move_x(self):
        for x in range(len(self.paddle_inventory_up) - 1, 0, -1):
            new_x = self.paddle_inventory_up[x - 1].xcor()
            new_y = self.paddle_inventory_up[x - 1].ycor()
            self.paddle_inventory_up[x].goto(new_x, new_y)
        self.paddle_inventory_up[0].fd(25)

    def move_up(self):
        #print(self.paddle_inventory_up)
        self.paddle_inventory_up[0].setheading(90)
        #self.paddle_inventory[0].fd(40)
        self.move_x()

    def move_down(self):
        #self.paddle_inventory = self.paddle_inventory[::1]
        self.paddle_inventory[0].setheading(270)
        self.move()






