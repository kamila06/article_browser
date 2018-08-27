import turtle

def draw_figures():
    window = turtle.Screen()
    window.bgcolor('yellow')
    hades = turtle.Turtle()
    hades.shape('turtle')
    hades.color('purple')
    for i in range(0, 4):
        hades.forward(100)
        hades.rt(90)

    hera = turtle.Turtle()
    hera.shape('turtle')
    hera.color('red')
    hera.circle(100)

    zeus = turtle.Turtle()
    zeus.shape('turtle')
    zeus.color('green')
    for i in range(0, 3):
        zeus.forward(300)
        zeus.left(120)

    hades = turtle.Turtle()
    hades.shape('turtle')
    hades.color('orange')
    for i in range(0, 360):
        hades.forward(10)
        hades.rt(1)

    window.exitonclick()

draw_figures()