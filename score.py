from turtle import Turtle


class Score():

    def score_x(self):
        score_x = Turtle()
        score_x.penup()
        score_x.goto(-80, 250)
        score_x.color("white")
        score_x.hideturtle()
        return score_x

    def score_y(self):
        score_y = Turtle()
        score_y.penup()
        score_y.goto(80, 250)
        score_y.color("white")
        score_y.hideturtle()
        return score_y




