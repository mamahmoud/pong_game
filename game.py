"""
This is a python pong game using turtle
"""
import turtle


def paddle_1_up():
    """
    This is a func to move pong up
    """
    y_axis = paddle_1.ycor()
    y_axis += 25
    if y_axis < 275:
        paddle_1.sety(y_axis)
    return


def paddle_1_down():
    """
    This is a func to move pong down
    """
    y_axis = paddle_1.ycor()
    y_axis -= 25
    if y_axis > -275:
        paddle_1.sety(y_axis)
    return


def paddle_2_up():
    """
    This is a func to move pong up
    """
    y_axis = paddle_2.ycor()
    y_axis += 25
    if y_axis < 275:
        paddle_2.sety(y_axis)
    return


def paddle_2_down():
    """
    This is a func to move pong down
    """
    y_axis = paddle_2.ycor()
    y_axis -= 25
    if y_axis > -275:
        paddle_2.sety(y_axis)
    return


if __name__ == "__main__":
    new_window = turtle.Screen()
    new_window.setup(width=800, height=600)
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
    paddle_1.goto(-380, 0)
    # paddle 1
    paddle_2 = turtle.Turtle()
    paddle_2.color("white")
    paddle_2.shape("square")
    paddle_2.speed(0)
    paddle_2.shapesize(5, 1)
    paddle_2.penup()
    paddle_2.goto(380, 0)
    # ball
    ball = turtle.Turtle()
    ball.color("green")
    ball.shape("circle")
    ball.speed(0)
    ball.penup()
    ball.dx = 0.2
    ball.dy = 0.2
    # keys
    new_window.listen()
    new_window.onkeypress(paddle_1_up, "w")
    new_window.onkeypress(paddle_1_down, "s")
    new_window.onkeypress(paddle_2_up, "Up")
    new_window.onkeypress(paddle_2_down, "Down")
    # score
    score_turtle = turtle.Turtle()
    score_turtle.penup()
    score_turtle.color("green")
    score_turtle.goto(0, 260)
    score_turtle.hideturtle()
    score_turtle.speed(0)
    score_1 = 0
    score_2 = 0
    while True:
        new_window.update()
        # print score
        score_turtle.clear()
        score_turtle.write(
            f"Player1 = {score_1}, Player2 = {score_2}",
            align="center",
            font=("Arial", 24, "normal"),
        )
        # move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # detect edge
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1
        if ball.xcor() > 390:
            score_1 += 1
            ball.dx *= -1
        if ball.xcor() < -390:
            score_2 += 1
            ball.dx *= -1
        # detect paddle2
        if (abs(ball.ycor() - paddle_2.ycor()) < 50) and (
            abs(ball.xcor() - paddle_2.xcor()) < 20
        ):
            ball.dy *= -1
            ball.dx *= -1
        # detect paddle2
        if (abs(ball.ycor() - paddle_1.ycor()) < 50) and (
            abs(ball.xcor() - paddle_1.xcor()) < 20
        ):
            ball.dy *= -1
            ball.dx *= -1
