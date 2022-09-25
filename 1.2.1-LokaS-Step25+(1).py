# a121_catch_a_turtle.py
#Clickthespotgame
#This program is intended to create a new spot in a random location after the spot is clicked by the mouse. The score will be scored after each click. 
#
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
shapespot = "circle"
colorspot = "blue"

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shapespot)
spot.shapesize(4,4)
spot.fillcolor(colorspot)
spot.speed(0)


#-----game functions--------

def change_position(new_xpos,new_ypos):
    new_xpos = rand.randint(-350,350)
    new_ypos = rand.randint(-350,350)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()

def spot_clicked(a, b):
    change_position(rand.randint(-400,400),rand.randint(-400,400))


#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()
