"""Minecraft snowman to the best of my ability."""
 
__author__ = "730602218"
 
from turtle import Turtle, done 


def draw_sm_square(alvin: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square."""
    alvin.penup()
    alvin.goto(x, y)
    alvin.setheading(0.0)
    alvin.pendown()
    i: int = 0
    while i < 4:
        alvin.forward(width)
        alvin.right(90)
        i = i + 1


def triangle_eye1(eye1: Turtle, x: float, y: float, width: float) -> None: 
    """Draw eye number 1."""
    eye1.begin_fill()
    eye1.penup()
    eye1.goto(x, y)
    eye1.pendown()
    i: int = 0
    while (i < 3):
        eye1.forward(width)
        eye1.left(120)
        i = i + 1
    eye1.end_fill()


def draw_md_square(simon: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square."""
    simon.penup()
    simon.goto(x, y)
    simon.setheading(0.0)
    simon.pendown()
    i: int = 0
    while i < 4:
        simon.forward(width)
        simon.right(90)
        i = i + 1


# def draw_lg_square(theodore: Turtle, x: float, y: float, width: float) -> None:
#     """Draw a square."""

def draw_lg_square(theodore: Turtle, x: float, y: float, width: float, depth: float) -> None:
    """Draw a square with recursion."""
    if depth == 0:
        return
    else:
        theodore.penup()
        theodore.goto(x, y)
        theodore.setheading(0.0)
        theodore.pendown()
        i: int = 0
        while i < 4:
            theodore.forward(width)
            theodore.right(90)
            i = i + 1
        return draw_lg_square(theodore, x + 50, y - 50, width / 2, depth - 1)


def main() -> None:
    """The entrypoint of my scene."""
    alvin: Turtle = Turtle()
    alvin.color("red")
    simon: Turtle = Turtle()
    simon.color("blue")
    simon.fillcolor("blue")
    theodore: Turtle = Turtle()
    theodore.color("green")
    eye1: Turtle = Turtle()
    eye1.fillcolor("black")
    # m: Turtle = Turtle()
    # mouth(m, -55, 230, 0)
    draw_sm_square(alvin, -75, 300, 100)
    triangle_eye1(eye1, -55, 255, 20)
    triangle_eye1(eye1, -15, 255, 20)
    draw_md_square(simon, -100, 200, 150)
    draw_lg_square(theodore, -125, 50, 200, 3)
    alvin.hideturtle()
    simon.hideturtle()
    theodore.hideturtle()
    eye1.hideturtle()
    done()


if __name__ == "__main__": 
    main()