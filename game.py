"""
This is a python pong game using turtle
"""
import turtle


def paddle_1_up():
    """
    This is a func to move pong up
    """
    y_axis = paddle_1.ycor()
    y_axis += 10
    if y_axis < 400:
        paddle_1.sety(y_axis)
    return


def paddle_1_down():
    """
    This is a func to move pong down
    """
    y_axis = paddle_1.ycor()
    y_axis -= 10
    if y_axis > -400:
        paddle_1.sety(y_axis)
    return


def paddle_2_up():
    """
    This is a func to move pong up
    """
    y_axis = paddle_2.ycor()
    y_axis += 10
    if y_axis < 400:
        paddle_2.sety(y_axis)
    return


def paddle_2_down():
    """
    This is a func to move pong down
    """
    y_axis = paddle_2.ycor()
    y_axis -= 10
    if y_axis > -400:
        paddle_2.sety(y_axis)
    return


if __name__ == "__main__":
    new_window = turtle.Screen()
    new_window.screensize(800, 600)
    new_window.bgcolor("orange")
    new_window.title("Mohamed Pong Game")
    new_window.tracer(0)

    # paddle 1
    paddle_1 = turtle.Turtle()

    paddle_1.color("white")
    paddle_1.shape("square")
    paddle_1.speed(0)
    paddle_1.shapesize(5, 1)
    paddle_1.penup()
    paddle_1.goto(-400, 0)
    # paddle 1
    paddle_2 = turtle.Turtle()
    paddle_2.color("white")
    paddle_2.shape("square")
    paddle_2.speed(0)
    paddle_2.shapesize(5, 1)
    paddle_2.penup()
    paddle_2.goto(400, 0)

    # ball
    ball = turtle.Turtle()
    ball.color("green")
    ball.shape("circle")
    ball.speed(0)
    ball.penup()

    # keys
    new_window.listen()
    new_window.onkeypress(paddle_1_up, "w")
    new_window.onkeypress(paddle_1_down, "s")
    new_window.onkeypress(paddle_2_up, "Up")
    new_window.onkeypress(paddle_2_down, "Down")
    while True:
        new_window.update()
