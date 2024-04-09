from turtle import Turtle, colormode, done


leo: Turtle = Turtle()


# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

# makes square
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1

# makes triangle
def triangle(leo: Turtle, x: float, y: float) -> None: 
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    i: int = 0
    while (i < 3):
        leo.forward(300)
        leo.left(120)
        i = i + 1


 
done()