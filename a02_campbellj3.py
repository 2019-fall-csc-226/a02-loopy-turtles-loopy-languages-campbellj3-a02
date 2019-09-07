# Author:     Jeremy Campbell
# Username:   campbellj3

# Assignment: a02
# Purpose: Demonstrating capacitites using the turtle program to bring joy.
# This program was modeled after the a02_triple_turtles.py file, created by Emily Lovell and Scott Heggen.

##########################################################################################################

import turtle       # Accessing the turtle library.
wn = turtle.Screen()
wn.bgcolor('grey') # Setting the background color to grey.
wn.title('Spooky Turtle Army!')

hallow_turtle = turtle.Turtle()    # Establishing the name for the turtle we will use
hallow_turtle.speed(15)
hallow_turtle.penup()
hallow_turtle.shape('turtle')

height = 90
width = 105
depth = 17

colors = ['orange', 'black', 'orange', 'black', 'orange', 'black']
# Telling the program which color scheme we will be using

for row in range(6):  # This line of code is indicating where the turtle will stamp, how many rows it will be in, and how wide those columns are
    hallow_turtle.color(colors[row])
    for col in range(6):
        for dep in range(6):
            hallow_turtle.goto(col * width - 300 + dep * depth, row * height - 300 + dep * depth * 1.3)
            hallow_turtle.stamp()

wn.exitonclick()