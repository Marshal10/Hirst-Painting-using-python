import colorgram
from turtle import *
from random import choice

turtle=Turtle()
screen=Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.speed("fastest")

colors=colorgram.extract('image.jpg',30)
rgb=[]
index=0

for color in colors:
    rgb.append(color.rgb)
    
def random_color():
    return choice(rgb)
    
def draw_row():
    for i in range(10):
        turtle.pendown()
        
        turtle.dot(20,random_color())
        turtle.penup()
        turtle.forward(50)    
        
def change_row(prev_pos):
    turtle.setpos(prev_pos)
    turtle.left(90)
    turtle.penup()
    turtle.forward(50)  
    turtle.right(90)  

def stop_painting():
    return index==10
    
stop=stop_painting()
while not stop:
    prev_pos=turtle.pos()
    draw_row()
    change_row(prev_pos)    
    index+=1
    stop=stop_painting()
    
screen.exitonclick()   