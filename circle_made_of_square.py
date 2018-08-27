import turtle

def draw_circle_made_of_square():
    window = turtle.Screen()
    window.bgcolor('yellow')
    hades = turtle.Turtle()
    hades.shape('turtle')
    hades.color('purple')
    for i in range(0, 60):
        for i in range(0, 4):
            hades.forward(100)
            hades.rt(90)
        hades.rt(10)
    window.exitonclick()

draw_circle_made_of_square()