import turtle
import winsound
from threading import Thread
import time

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgpic("./movementsprite/bg.gif")
counter = 0
wn.bgcolor("black")
neutral= "./movementsprite/neutral.gif"
forward_1 ="./movementsprite/forward_1.gif"
forward_2 ="./movementsprite/forward_2.gif"
neutralreverse ="./movementsprite/neutralreverse.gif"
reverse_1 ="./movementsprite/reverse_1.gif"
reverse_2 ="./movementsprite/reverse_2.gif"
turtle.penup()
turtle.addshape(name = neutral,shape=None)
turtle.addshape(name = forward_1,shape=None)
turtle.addshape(name = forward_2,shape=None)
turtle.addshape(name = neutralreverse,shape=None)
turtle.addshape(name = reverse_1,shape=None)
turtle.addshape(name = reverse_2,shape=None)
turtle.shape(neutral)
turtle.sety(-240)

def play_sound():
    winsound.PlaySound("./movementsprite/song.wav", winsound.SND_ASYNC)
def right(): 
    turtle.forward(10)
    run_right()
def left():
    turtle.back(10)
    run_left()

def stand_left():
    counter = 0
    turtle.shape(neutral)

def stand_right():
    counter = 0
    turtle.shape(neutralreverse)
def run_left():
    global counter
    if counter >= 0 and counter < 12 :
        counter += 6
        turtle.shape(forward_1)
    elif counter >= 12 and counter < 24:
        counter += 6
        turtle.shape(forward_2)
    elif counter >= 24:
        counter = 0

def run_right():
    global counter
    if counter >= 0 and counter < 12 :
        counter += 6
        turtle.shape(reverse_1)
    elif counter >= 12 and counter < 24:
        counter += 6
        turtle.shape(reverse_2)
    elif counter >= 24:
        counter = 0
play_sound()
while True : 
    wn.update()

    turtle.listen() 
    turtle.onkeypress(left,"Left")
    turtle.onkeypress(right,"Right")
    turtle.onkeyrelease(stand_left,"Left")
    turtle.onkeyrelease(stand_right,"Right")