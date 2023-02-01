import turtle as t
import random
import time

# width * height
t.setup(width=800, height=800)
t.shape('turtle')
t.color('orange')
t.bgcolor('blue')

# make the center line
t.goto(0,400)
t.goto(0,-400)
t.goto(0,0)

# change the speed
t.speed(1)

# pen up
t.penup()

for i in range(10):
    t.forward(random.randint(-50, 50))
    time.sleep(1)
    
if t.xcor() > 0:
    t.write("turtle goes eight", font = ('Arial', 16))
elif t.xcor < 0:
    t.write("turtl goes left", font = ('Arial', 16))
else:
    t.write("turtle goes center", font = ('Arial', 16))

# exit when you click the screen
t.exitonclick()