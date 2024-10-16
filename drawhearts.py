import turtle

def heart (turtle, size, color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.left(140)
    turtle.forward(size)

    turtle.circle(-size // 2, 200)

    turtle.left(120)
    turtle.circle(-size // 2, 200)

    turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)

def draw_hearts ():
    turtle.bgcolor('lightpink')
    turtle.speed(4)
    turtle.width(3)

    sizes = [250, 200, 150, 100, 50]
    colors = ['#E57582', '#E793A2', '#DCB7BB', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors):
        turtle.penup()
        turtle.goto(0, -size // 2)
        turtle.pendown()
        heart(turtle, size, color)

    turtle.hideturtle()
    turtle.done()

draw_hearts()