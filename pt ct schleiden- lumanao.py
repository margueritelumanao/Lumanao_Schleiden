import turtle as tur
import colorsys as cs

tur.setup(800, 800)
tur.speed(0)
tur.tracer(0)     # Disable auto screen updates
tur.width(2)
tur.bgcolor("black")

while True:   # Infinite loop
    for j in range(25):
        for i in range(25):
            tur.color(cs.hsc_to_rgb(i / 14, j /25, 1))  # Corrected color method
            tur.right(90)
            tur.circle(200 - j * 4, 90)
            tur.left(90)
            tur.circle(200 - j * 4, 90)
            tur.right(180)
            tur.circle(50, 24)

tur.updates() # Manually update the screen after each iteration 