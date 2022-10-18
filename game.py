"""
This is a python pong game using turtle
"""
import turtle


def paddle_1_up():
    y = paddle_1.ycor()
    y += 10
    if y < 400:
        paddle_1.sety(y)
    return


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 10
    if y > -400:
        paddle_1.sety(y)
    return


def paddle_2_up():
    y = paddle_2.ycor()
    y += 10
    if y < 400:
        paddle_2.sety(y)
    return


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 10
    if y > -400:
        paddle_2.sety(y)
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
    new_window.onkeypress(paddle_2_up, "UP")
    new_window.onkeypress(paddle_2_down, "DOWN")
    while True:
        new_window.update()
