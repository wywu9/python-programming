# 转义字符
print("He said, \"Jonh's program is easy to read\"")

# 不换行打印,参数end（默认状态下print自动打印换行符）
print("AAA",end = ' ')
print("BBB",end = '')
print("CCC",end = '***')
print("DDD",end = '***')

# 用+号进行字符串连接
s = "chapter " + str(3)
s += " is fun."

# format
print(format(2.3333989,".3f"))
print(round(2.3333989,3))
print(format(2.3333989,"10.2f"))

# circle
import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(40,steps=3)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(40,steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('green')
turtle.circle(40,steps=5)
turtle.end_fill()

turtle.penup()
turtle.goto(100,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(40,steps=6)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(40)
turtle.end_fill()

turtle.bye()

# 3.10
index_0=ord("\u03b1")
for i in range(8):
    print(chr(index_0+i),end='')

# 3.11
number=eval(input("Enter an integer:"))
reversedNumber=0
temp_index=0
while number != 0:
    temp_index += 1
    reversedNumber += (number%10)*(10**(4-temp_index))
    number //= 10
print("The reversed number is",reversedNumber)

# 3.12
import math,turtle
side=eval(input("Enter the side of star:"))
starVertexAngle=36
starInerAngle=360/5
starRadius=math.sqrt(side**2*(1-math.cos(math.radians(starVertexAngle)))
                     /(1-math.cos(math.radians(starInerAngle))))
turtle.penup()
turtle.goto(0,starRadius)
turtle.right(90+starVertexAngle/2)
turtle.pendown()
for i in range(5):
    turtle.forward(side)
    turtle.left(180-starVertexAngle)
turtle.bye()

# 3.12
import turtle
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.circle(200,steps=6)
turtle.end_fill()
turtle.penup()
turtle.goto(-90,-25)
turtle.pendown()
turtle.color("white")
turtle.write("STOP",font=("Times",50,"bold"))
turtle.hideturtle()
turtle.bye()

# 3.19
import turtle,math
x1,y1,x2,y2=eval(input("Enter two points:"))
distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
angle=math.fabs(math.degrees(math.atan((y2-y1)/(x2-x1))))
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write('('+str(x1)+','+str(y1)+')')
turtle.right(angle)
turtle.forward(distance)
turtle.write('('+str(x2)+','+str(y2)+')')




