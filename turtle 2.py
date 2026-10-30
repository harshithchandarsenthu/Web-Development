import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
def petal(colour):
    t.color(colour)
    t.begin_fill()
    for i in range(2):
        t.circle(60, 60)
        t.left(120)
    t.end_fill()
for colour in colours:
    for i in range(6):
        petal(colour)
        t.left(60)
    t.left(15)
t.hideturtle()
turtle.done()
