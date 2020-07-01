from turtle import *
import random
t = Turtle()
x = 0
setup(500, 500)

t.hideturtle()
t.speed(0)

for i in range(500):
    t.forward(5 * i)
    t.right(150)
# at right(x) x is the angle. you change it to 90 to get a square spiral, 120 for a triangle. you can apply a random.randrange func there and get some wacky results as well
