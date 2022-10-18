"""
This is a python pong game using turtle
"""
import turtle

if __name__ == "__main__":
    new_window = turtle.Screen()
    new_window.screensize(800, 600)
    new_window.bgcolor("orange")
    new_window.title("Mohamed Pong Game")
    new_window.tracer(0)
    while True:
        new_window.update()
