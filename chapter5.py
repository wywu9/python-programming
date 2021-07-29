# 显示素数
counter=0
number=2
lineMarker=0
print("The first 50 primes are:")
while counter<50:
    # 判断素数更适合用while循环而非for循环
    for i in range(2,number+1):
        if number!=2 and number%i==0:
            break
    if i>=int(number/2):
        print(format(number,"5d"),end='')
        lineMarker +=1
        counter += 1
    if lineMarker==10:
        print()
        lineMarker=0
    number += 1

# 随机行走
import turtle,random
x=-80
for y in range(-80,80+1,10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
y=80
turtle.right(90)
for x in range(-80,80+1,10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
turtle.penup()
turtle.home()
turtle.down()
turtle.color("red")
turtle.pensize(3)
x,y=0,0
while abs(x)<80 and abs(y)<80:
    direction=random.randint(0,3)
    if direction==0:
        turtle.setheading(0)
        turtle.forward(10)
        x+=10
    elif direction==1:
        turtle.setheading(90)
        turtle.forward(10)
        y+=10
    elif direction==2:
        turtle.setheading(180)
        turtle.forward(10)
        x-=10
    else:
        turtle.setheading(270)
        turtle.forward(10)
        y-=10
turtle.bye()

# 5.1
sentinel=1
positive=0
negative=0
total=0
summary=0
while sentinel==1:
    data=eval(input("Enter an integer, the input ends if it is 0:"))
    summary+=data
    if data==0:
        sentinel=0
    elif data>0:
        positive+=1
        total+=1
    else:
        negative+=1
        total+=1
if total>0:
    average=summary/total
    print("The number of positives is",positive)
    print("The number of negatives is",negative)
    print("The total is",total)
    print("The average is",average)
else:
    print("You didn't enter any number")

# 5.4
for i in range(11):
    print("-"*50)
    if i==0:
        print(' '*9,"英里",' '*9,'|',' '*9,"公里",' '*9)
    else:
        print(' '*10,i,' '*10,'|',' '*10,1.609*i,' '*10)
print("-"*50)

# 5.11
numberOfStudent=eval(input("Enter the number of students:"))
max1=0
max2=0
for i in range(numberOfStudent):
    grade=eval(input("Enter the scores one by one:"))
    if grade>max1:
        max1=grade
    elif grade<=max1 and grade>=max2:
        max2=grade
print("the first is",max1," and the second is",max2)

# 5.12
lineCounter=0
for i in range(100,1000+1):
    if i%5==0 and i%6==0:
        print(i,' ',end='')
        lineCounter += 1
    if lineCounter==10:
        lineCounter=0
        print()

# 5.13
lineCounter=0
for i in range(100,200+1):
    if (i%5==0 and i%6!=0) or (i%6==0 and i%5!=0):
            print(i,' ',end='')
            lineCounter += 1
    if lineCounter==10:
        lineCounter=0
        print()

# 5.14
n=100
nSquare=0
while nSquare <=12000:
    n += 1
    nSquare=n**2
print(n)

# 5.16
n1,n2=eval(input("Enter two integers:"))
if n1<n2:
    n1,n2=n2,n1
for i in range(n2,0,-1):
    if n1%i==0 and n2%i==0:
        print("The number is",i)
        break

# 5.17
low=ord("!")
high=ord("~")
lineCounter=0
for i in range(low,high+1):
    print(chr(i),' ',end='')
    lineCounter += 1
    if lineCounter==10:
        lineCounter=0
        print()

# 5.18
number=eval(input("Enter a integer:"))
temp=number
lineCounter=0
for i in range(2,number+1):
    j=2
    while j<=i/2:
        if i!=2 and j%i==0:
            break
        j +=1
    if j>i/2:
        while temp % i == 0:
            temp /= i
            print(' ',i,end=',')
            lineCounter+=1
            if lineCounter==10:
                lineCounter=0
                print()

# 5.19
number=eval(input("Enter the number of lines:"))
blank=0
startBlank=30
for i in range(1,number+1):
    for j in range(i,0,-1):
        if j==i:
            blank=startBlank-2*(i-1)
            print(format(j,str(eval("blank"))+'d'),end=' ')
        else:
            print(j,end=' ')
    for j in range(2,i+1):
        print(j,end=' ')
    print()

# 5.20
# modern A
for i in range(1,6+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# modern B
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# modern C
for i in range(1,6+1):
    print(' '*(2*(6-i)),end='')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

# modern D
for i in range(6,0,-1):
    print(' '*(2*(6-i)),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# 5.21
index=eval(input("Enter the number of lines:"))
for i in range(index+1):
    blank=4*(index-i)
    print(' '*blank,end='')
    for j in range(1,i+1):
        print(format(2**(j-1),'4d'),end='')
    for j in range(i+1,0,-1):
        print(format(2**(j-1),'4d'),end='')
    print()

# 5.22
lineCounter=0
for i in range(2,1000+1):
    j=2
    while j<=i/2:
       if i%j==0:
           break
       else:
           j+=1
    if j>i/2:
        print(format(i,'<4d'),end='')
        lineCounter+=1
    if lineCounter==8:
        lineCounter=0
        print()

# 5.23
loan=eval(input("Loan Amount:"))
year=eval(input("Number of years:"))
yearRate=0.05
delta=1/800
print(format("Interest Rate",'20s'),format("Monthly Payment",'20s'),
      format("Total Payment",'20s'),end='\n')
# warn! 如果循环终止条件设为0.08，就会出现1的误差，
# 因为浮点数最后一个为0.0800003，略大于0.8，因此导致漏掉了一个值
while yearRate <= (0.08+delta/2):
    monthlyRate=yearRate/12
    monthlyPayment=loan*monthlyRate/(1-1/(1+monthlyRate)**(year*12))
    totalPayment=monthlyPayment*year*12
    print(format(yearRate,'<20.3%'),format(monthlyPayment,'<20.2f'),
          format(totalPayment,'<20.2f'),end='\n')
    yearRate += delta

# 5.24
loan=eval(input("Loan Amount:"))
year=eval(input("Number of Years:"))
yearRate=0.01*eval(input("Annual Interest Rate:"))
monthlyRate=yearRate/12
monthlyPayment=loan*monthlyRate/(1-1/(1+monthlyRate)**(year*12))
totalPayment=monthlyPayment*year*12
balance=loan
print("Monthly Payment:",format(monthlyPayment,'.2f'))
print("Total Payment:",format(totalPayment,'.2f'))
print(format("Payment#",'15s'),format("Interest",'15s'),
      format("Principal",'15s'),format("Balance",'15s'))
for i in range(1,year*12+1):
    interest=balance*monthlyRate
    principal=monthlyPayment - interest
    balance -= principal
    print(format(i,'<15d'),format(interest,'<15.2f'),
          format(principal,'<15.2f'),format(balance,'<15.2f'))

# 5.25
n=50000
sumSequence=0
sumReverse=0
for i in range(n,0,-1):
    sumReverse += 1/i
    sumSequence += 1/(n-i+1)
error=sumReverse - sumSequence
print(sumSequence,sumReverse,error,sep=' ')

# 5.27
for i in range(10000,100000+1,10000):
    pi=0
    for j in range(1,i+1):
        pi += 4*(-1)**(j+1)/(2*j-1)
    print("when i=",i,", pi=",pi)

# 5.28
for i in range(10**4,10**4+1,10**4):
    e=1
    item=1
    for j in range(1,i+1):
        item *= 1/j
        e += item
    print("when i=",i,", e=",e)

# 5.30
year,day=eval(input("Enter the year and its first weekday:"))
month=["January","February","March","April","May",
       "June","July","August","September","October",
       "November","December"]
week=["Monday","Tuesday","Wednesday",
      "Thursday","Friday","Saturday","Sunday"]
weekDay,monthDay=day,0
for i in range(1,12+1):
    weekDay=(monthDay%7+weekDay)%7
    if i in [1,3,5,7,8,10,12]:
        monthDay=31
    elif i in [4,6,9,11]:
        monthDay=30
    else:
        if (year%4==0 or year%100==0) and (year%400!=0):
            monthDay=29
        else:
            monthDay=28
    print(month[i-1],' 1, ',year," is ",week[weekDay-1])

# 5.35
for i in range(1,10000+1):
    j=1
    factorSummary=0
    while j<=i/2:
        if i%j==0:
            factorSummary += j
        j += 1
    if i==factorSummary:
        print(i)

# 5.36
import random
gesture=["rock","scissors","paper"]
counter1,counter2=0,0
while counter1 <=2 and counter2 <=2:
    user=eval(input("Enter 0-2(rock,scissors,paper respectively):"))
    computer=random.randint(0,2)
    if user==computer:
        print("It's a draw!")
    elif (user-computer) in [-1,2]:
        print("You won! The computer' gesture is ",gesture[computer])
        counter1 += 1
        counter2=0
    else:
        print("You lost.The computer' gesture is ",gesture[computer])
        counter2 += 1
        counter1=0
if counter1>2:
    print("You have lost for more than two times continuously. The game is over.")
else:
    print("You have won for two times continuously. The game is over.")

# 5.38
import time
seconds=eval(input("Enter the number of seconds:"))
while seconds >= 2:
    time.sleep(1)
    print(seconds-1,' seconds remaining')
    seconds -= 1
print("Stopped")

# 5.41
max,count=0,0
while True:
    number=eval(input("Enter a number (0: for end of input):"))
    if number == 0:
        break
    else:
        if number > max:
            max=number
            count=1
        elif number == max:
            count += 1
print("The largest number is ",max)
print("The occurrence count of the largest number is ",count)

# 5.42
SIZE=400
import random,turtle
turtle.penup()
turtle.goto(-SIZE/2,-SIZE/2)
turtle.pendown()
for i in range(4):
    turtle.forward(SIZE)
    turtle.left(90)
turtle.penup()
turtle.goto(0,-SIZE/2)
turtle.pendown()
turtle.left(90)
turtle.forward(SIZE)
turtle.setheading(315)
turtle.forward((SIZE/2)*2**0.5)
turtle.setheading(180)
turtle.forward(SIZE/2)
n=0
turtle.speed(10)
# turtle.color("blue")
# 模拟100次，10**6次太耗时了
simulTimes=10**2
for i in range(simulTimes):
    x=SIZE/2*(2*random.random()-1)
    y=SIZE/2*(2*random.random()-1)
    turtle.penup()
    turtle.goto(x,y-1)
    turtle.pendown()
    # dot的半径太小（如1） 画出的点看不见
    turtle.dot(5,"blue")
    if x<=0 or (x>=0 and x+y<50):
        n += 1
probEven=n/simulTimes
print(probEven)

# 5.44
length=0
decimalNumber=eval(input("Enter a decimal number:"))
binaryNumber=[]
while decimalNumber>0:
    binaryNumber.append(decimalNumber%2)
    decimalNumber //= 2
    length += 1
for i in range(length):
    print(str(binaryNumber[length-i-1]),end='')

# 5.45
decimalNumber=eval(input("Enter a decimal number:"))
hexaNumber=[]
length=0
while decimalNumber>0:
    temp=decimalNumber%16
    if temp in range(10):
        hexaNumber.append(temp)
    else:
        hexaNumber.append(chr(temp-10+ord('A')))
    decimalNumber //= 16
    length += 1
for i in range(length):
    print(hexaNumber[length-i-1],end='')

# 5.52
import turtle,math
xAxe=400
yAxe=100
arrow=20
turtle.penup()
turtle.goto(-xAxe/2,0)
turtle.pendown()
turtle.forward(xAxe)
turtle.setheading(150)
turtle.forward(arrow)
turtle.backward(arrow)
turtle.setheading(210)
turtle.forward(arrow)

turtle.penup()
turtle.goto(0,-yAxe/2)
turtle.setheading(90)
turtle.pendown()
turtle.forward(yAxe)
turtle.setheading(240)
turtle.forward(arrow)
turtle.backward(arrow)
turtle.setheading(300)
turtle.forward(arrow)

turtle.setheading(0)


turtle.pendown()
for x in range(-175,176):
    if x==-175:
        turtle.penup()
        turtle.goto(x,50*math.sin((x/100)*2*math.pi))
        turtle.pendown()
    else:
        turtle.goto(x,50*math.sin((x/100)*2*math.pi))

turtle.penup()
turtle.goto(-100,-15)
turtle.pendown()
turtle.write("-2\u03c0")
turtle.penup()
turtle.goto(100,-15)
turtle.pendown()
turtle.write("2\u03c0")
turtle.bye()

# 5.55
import turtle
size=50
gridNumber=8
side=size*8
for i in range(1,gridNumber+2):
    turtle.penup()
    turtle.goto(-side/2,size*(5-i))
    turtle.pendown()
    turtle.forward(side)
turtle.right(90)
for i in range(1,gridNumber+2):
    turtle.penup()
    turtle.goto(size*(5-i),side/2)
    turtle.pendown()
    turtle.forward(side)
turtle.color("black")
turtle.setheading(0)
for i in range(1,9):
    for j in range(1,9):
        if (i in range(1,8,2) and j in range(2,9,2))\
        or (i in range(2,9,2) and j in range(1,8,2)):
            turtle.penup()
            turtle.goto(-size*(4-j+1),size*(4-i+1))
            turtle.pendown()
            turtle.begin_fill()
            for k in range(4):
                turtle.forward(size)
                turtle.right(90)
            turtle.end_fill()









