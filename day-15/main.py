"""
Day 15 - Instances, Objects and Turtle
Intro to the turtle graphics module: drawing shapes and a random
walk pattern using an object (Turtle instance).
"""
import turtle as turtle_module
import random

timmy = turtle_module.Turtle()
screen = turtle_module.Screen()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


# Draw shapes with 3 to 10 sides
for shape_side_n in range(3, 11):
    random_color = (random.random(), random.random(), random.random())
    timmy.color(random_color)
    draw_shape(shape_side_n)

# Reset and do a random walk pattern
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
timmy.speed("fastest")

directions = [0, 90, 180, 270]
for _ in range(200):
    timmy.pencolor((random.random(), random.random(), random.random()))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen.exitonclick()
