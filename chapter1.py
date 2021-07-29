# 1.6节
# 1.1
print('Welcome to python')
print('Welcome to computer science')
print('Programming is fun')

# 1.2
print('Welcome to python\n'*5)

# 1.3
print('F'*7,'  ','U     U','  ','NN    NN')
print('FF     ','  ','U     U','  ','NNN   NN')
print('F'*7,'  ','U     U','  ','NN N  NN')
print('FF     ','  ',' U   U ','  ','NN  N  NN')
print('FF     ','  ','  UUU  ','  ','NN    NNN')

# 1.4
for i in range(5):
    if i==0:
        print('a    ','a^2    ','a^3    ')
    else:
        print(i,'    ',i**2,'    ',i**3,'    ')

# 1.5
print((9.5*4.5-2.5*3)/(45.5-3.5))

# 1.6
sum=0
for i in range(1,10):
    sum=sum+i
print(sum)

# 1.7
pi=0
for i in range(6):
   pi=pi+1/(2*i+1)*(-1)**i
print(pi*4)

pi=0
for i in range(8):
    pi=pi+1/(2*i+1)*(-1)**i
print(pi*4)

# plus,循环次数越大越接近真实值
'''
pi=0
for i in range(1000000):
    pi=pi+1/(2*i+1)*(-1)**i
print(pi*4)
'''
# 1.8
r=5.5
pi=3.14
area=r*r*pi
perimeter=2*r*pi
print(area,perimeter)

# 1.9
w=4.9
h=7.9
area=w*h
print(area)

# 1.10
time=45.5/60
distance=14/1.6
v=distance/time
print(v)

# 1.11
num_start=3120324986
num_future=[]
year_time=365*24*60*60 # s
increment=year_time//7+year_time//45-year_time//13
for i in range(1,6):
    num_temp=num_start+increment*i
    print(num_temp)


# 1.9节
# 1.12
import turtle
turtle.penup()
turtle.goto(-50,50)
turtle.pendown()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.penup()
turtle.goto(50,0)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.done()

# 1.15
import turtle
turtle.penup()
turtle.right(60)
turtle.pendown()
turtle.forward(50)
for i in range(2):
    turtle.right(120)
    turtle.forward(50)
turtle.forward(50)
for i in range(2):
    turtle.left(120)
    turtle.forward(50)
turtle.bye()

# 1.21
import turtle
turtle.forward(50)
turtle.penup()
turtle.goto(0,0)
turtle.left(90)
turtle.pendown()
turtle.forward(60)
turtle.penup()
turtle.goto(0,-85)
turtle.right(90)
turtle.pendown()
turtle.circle(85)

turtle.penup()
turtle.goto(0,70)
turtle.pendown()
turtle.write(12)

turtle.penup()
turtle.goto(70,0)
turtle.pendown()
turtle.write(3)

turtle.penup()
turtle.goto(0,-70)
turtle.pendown()
turtle.write(6)

turtle.penup()
turtle.goto(-70,0)
turtle.pendown()
turtle.write(9)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.write('9:15:00')
turtle.bye()








