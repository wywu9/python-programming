# input函数，eval函数
radius=eval(input('please enter a value for radius:'))
area=radius*radius*3.14159
print('the area for the circle of radius',radius,'is',area)

# time
import time
currentTime=time.time()
totalSeconds=int(currentTime)

# 编程题
# 2.1
celsius=eval(input('Enter a degree in Celsius:'))
fahrenheit=(9/5)*celsius+32
print(celsius,'Celsius is',fahrenheit,'Fahrenheit')

# 2.2
pi=3.1415926
radius,length=eval(input('Enter the radius and length of a cylinder:'))
area=radius*radius*pi
volume=area*length
print('The area is',area)
print('The volume is',volume)

# 2.5
subtotal,gratuity_rate=eval(input('Enter the subtotal and a gratuity rate:'))
gratuity=int((subtotal*gratuity_rate/100)*100)/100.0
total=(int(subtotal+gratuity))*100/100.0 # 保留两位小数
print('The gratuity is',gratuity,'and the total is',total)

# 2.6
test_number = eval(input('Enter a number between 0 and 1000:'))
sum=0
while test_number != 0:
    temp_number = test_number%10
    test_number //= 10
    sum +=temp_number
print('The sum of the digits is',sum)

# 2.7
minutes = eval(input('Enter the number of minutes:'))
hours = minutes // 60
days = hours // 24
years = days // 365
remain_days = days % 365
print(minutes,'minutes is approximately',years,'years and',remain_days,'days')

# 2.11
finalAccount = eval(input('Enter final account:'))
annualInterestRate = eval(input('Enter annual interest rate in percent:'))
years = eval(input('Enter number of years:'))
initialAccount = finalAccount / (1 + annualInterestRate / (100 * 12)) ** (years * 12)
print('Initial deposit value is',initialAccount)

#2.13
# 也可以使用算术符号//和%
number=reversed(list(input('Enter an integer:')))
for i in number:
    print(int(i))

# 2.14
import math
x1,y1,x2,y2,x3,y3=eval(input('Enter three points for a triangle:'))
side1=math.sqrt(((x2-x3)**2+(y2-y3)**2))
side2=math.sqrt(((x1-x3)**2+(y1-y3)**2))
side3=math.sqrt(((x2-x1)**2+(y2-y1)**2))
s=(side1+side2+side3)/2
area=int(math.sqrt(s*(s-side1)*(s-side2)*(s-side3))*100)/100.0
print('The area of the triangle is',area)

# 2.21
savingMonthly=eval(input('Enter the monthly saving amount:'))
interestRateMonthly=0.05/12
amount=0
for i in range(6):
    amount += savingMonthly
    amount *= 1+ interestRateMonthly
print('After the sixth month, the account value is',int(amount*100)/100.0)

# 2.25
x,y,width,height=eval(input('Enter the center and size of a rectangle:'))
import turtle
turtle.penup()
turtle.goto(x-width/2,y-height/2)
turtle.pendown()
for i in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
turtle.bye()

# 2.26
x,y,radius=eval(input('Enter the center and radius of the circle:'))
import turtle
turtle.penup()
turtle.goto(x,y-radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.write(radius*radius*3.1415926)
turtle.bye()



