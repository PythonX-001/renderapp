from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import latex2mathml.converter
import random
latex_input = "arctan(x^2-1/2x) + arctan(1/x) = arctan((x^2-1/2x + 1/x)/(1 - x^2/2))"
mathml_output = latex2mathml.converter.convert(latex_input)
import time
from lexica import Client

def main(model_id:int,prompt:str,negative_prompt:str) -> dict:
    client = Client()
    resp = client.generate(model_id,prompt,negative_prompt)
    print(resp)
    task_id = resp['task_id']
    request_id = resp['request_id']
    time.sleep(100) # sleep for period of time to allow the task to be processed
    response = client.getImages(task_id,request_id)
    return response



import turtle
import time

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Love Story in the Stars')

t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.color('white')

# Draw the stars
import turtle
import time

# Set up the screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('lightpink')
screen.title('Dancing Hearts')

t1 = turtle.Turtle()
t1.speed(0)
t1.pensize(2)
t1.color('red')

t2 = turtle.Turtle()
t2.speed(0)
t2.pensize(2)
t2.color('pink')

# Draw the hearts
t1.penup()
t1.goto(-150, 0)
t1.pendown()
for i in range(3):
    t1.forward(20)
    t1.right(120)

t2.penup()
t2.goto(150, 0)
t2.pendown()
for i in range(3):
    t2.forward(20)
    t2.right(120)

# Make the hearts dance
while True:
    # Move the first heart
    t1.penup()
    t1.forward(20)
    t1.pendown()
    t1.right(10)

    # Move the second heart
    t2.penup()
    t2.backward(20)
    t2.pendown()
    t2.left(10)

    time.sleep(0.1)
turtle.mainloop()
