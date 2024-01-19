import turtle

import colorsys

turtle.bgcolor("black")

turtle.tracer(10)

hue = 0.1

turtle.ht()

for i in range(400):
    color = colorsys.hsv_to_rgb(hue,1,1)
    turtle.color(color)
    hue+= 0.004
    turtle.fd(i)
    turtle.rt(91)
    turtle.bk(i/2)
    turtle.lt(40)