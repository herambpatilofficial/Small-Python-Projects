from turtle import Turtle, Screen, setpos
import random
name = Turtle()



name.shape("circle")

name.speed(0)

for i in range(0, 360):
    
    tup = (random.uniform(0.0,1.0) , random.uniform(0.0,1.0), random.uniform(0.0,1.0))
    name.pencolor(tup)

    name.left(int(i))

    name.circle(100)




screen = Screen()
screen.exitonclick()


