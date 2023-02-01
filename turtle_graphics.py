import turtle as t

# 거북이 모양으로 변경
t.shape('turtle')

# change the color
t.color('orange')
t.bgcolor('blue')

# go forward
t.forward(200) # 200px 만큼 앞으로

# speed 1 ~ 10
t.speed(1)

# change the direction
t.left(90)
t.forward(200)

# 특정 좌표료 이동
t.goto(30, 100)

# pen up
t.penup()
t.forward(-200)

# 화면을 클릭할 때 종료
t.exitonclick()
