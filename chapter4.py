# leap year
year = eval(input("Enter a year: "))
isLeapYear = (year % 4 == 0 and year % 100 !=0) \
    or (year % 400 == 0)
print(year,"is a leap year?",isLeapYear)

# 4.1
a,b,c=eval(input("Enter a,b,c:"))
delta=b**2-4*a*c
if delta>0:
    r1=(-b+delta**0.5)/(2*a)
    r2=(-b-delta**0.5)/(2*a)
    print("The roots are",r1,"and",r2)
elif delta==0:
    r1=(-b+delta**0.5)/(2*a)
    print("The root is",r1)
else:
    print("The equation has no real roots")

# 4.4
import random
digit1=random.randint(0,99)
digit2=random.randint(0,99)
sumGuess=eval(input("Please add "+str(digit1)+','+str(digit2)+\
                    " and enter the summary:"))
judgeGuess=(digit1+digit2)==sumGuess
if judgeGuess == 1:
    print("Your answer is right!")
else:
    print("Your answer is wrong, and the true answer is ",digit1+digit2)

# 4.5
week=["Sunday","Monday","Tuesday",
      "Wednesday","Thursday","Friday","Saturday"]
today=eval(input("Enter today's day:"))
daysNumber=eval(input("Enter the number of days elapsed since today:"))
print("Today is ",week[today],
      " and the future day is ",week[(today+daysNumber)%7])

# 4.8
a,b,c=eval(input("Enter 3 integer:"))
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a,b,c)

# 4.11
month31=[1,3,5,7,8,10,12]
month30=[4,6,9,11]
month,year=eval(input("Enter the month and year:"))
days=0
if month in month30:
    days = 30
elif month in month31:days = 31
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
print("year",year,"month",month,"has",days,"days")

# 4.17
import random
sign=["scissor","rock","paper"]
scissor=0
rock=1
paper=2
player=eval(input("scissor(0), rock(1), paper(2):"))
computer=random.randint(0,2)
judge=["You won","It is a draw","You lost"]
if (player-computer) in [1,-2]:
    print("The computer is ",sign[computer],
          ". You are ",sign[player],". ",judge[0])
elif player==computer:
    print("The computer is ",sign[computer],
          ". You are ",sign[player],". ",judge[1])
else:
    print("The computer is ",sign[computer],
          ". You are ",sign[player],". ",judge[2])

# 4.19
a,b,c=eval(input("Enter three edges:"))
if a+b>c and a+c>b and b+c>a:
    print("The perimeter is",a+b+c)
else:
    print("The input is invalid")

# 4.21
week=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
year=eval(input("Enter year: (e.g., 2008):"))
month=eval(input("Enter month: 1-12:"))
day=eval(input("Enter the day of the month: 1-31:"))
j=(year/100)//1
k=(year%100-1) if month in [1,2] else year%100
m=month+12 if month in [1,2] else month
q=day
h=(q+(26*(m+1)/10)//1+k+(k/4)//1+(j/4)//1+5*j)%7
print("Day of the week is ",week[int(h)])

# 4.24
# 也可使用随机生成两个整数的方法
import collections,random
Card=collections.namedtuple("Card",["rank","shape"])
class sophieDeck:
    ranks=["Ace"]+list(range(2,11))+["Jack","Queen","King"]
    shapes=["spades","diamonds","clubs","hearts"]

    def __init__(self):
        self._cards=[Card(rank,shape) for rank in self.ranks
                     for shape in self.shapes]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]
choice=random.randint(0,51)
deck=sophieDeck()
rank=deck[choice][0]
shape=deck[choice][1]
print("The card you picked is the ",rank,"of ",shape)

# 4.25
x1,y1,x2,y2,x3,y3,x4,y4=eval(input("Enter x1,y1,x2,y2,x3,y3,x4,y4:"))
a=y1-y2
b=x2-x1
c=y3-y4
d=x4-x3
e=(y1-y2)*x1-(x1-x2)*y1
f=(y3-y4)*x3-(x3-x4)*y3
if a*d-b*c==0:
    print("The two lines are parallel")
else:
    x=(e*d-b*f)/(a*d-b*c)
    y=(a*f-e*c)/(a*d-b*c)
    print("The intersecting point is at (",x,',',y,')')

# 4.27
x,y=eval(input("Enter a point's x- and y-coordinates:"))
# y=-1/2*x+100 即 2y+x-200=0
if x>=0 and y>=0 and 2*y+x-200<=0:
    print("The point is in the triangle")
else:
    print("The point is not in the triangle")

# 4.28
x1,y1,w1,h1=eval(input("Enter r1\'s center x-, \
y-coordinates, width, and height:"))
x2,y2,w2,h2=eval(input("Enter r2\'s center x-, \
y-coordinates, width, and height:"))
if abs(x2-x1)<=(w1-w2)/2 and abs(y2-y1)<=(h1-h2)/2:
    print("r2 is inside r1")
elif abs(x2-x1)>=w1+w2/2 and abs(y2-y1)>=h1+h2/2:
    print("r2 does not overlap r1")
else:
    print("r2 overlaps r1")

# 4.33
decimal=eval(input("Enter a decimal value (0 to 15):"))
if decimal<=9:
    print("The hex value is",decimal)
elif decimal<=15:
    print("The hex value is ",chr(ord('A')+decimal-10))
else:
    print("Invalid input")

# 4.36
import turtle
x,y=eval(input("Enter x-, y-coordinates of a point:"))
w=100
h=50
inside=abs(x)<=w/2 and abs(y)<=h/2
status=["inside","not inside"]
turtle.penup()
turtle.goto(-w/2,-h/2)
turtle.pendown()
for i in range(2):
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
turtle.penup()
turtle.goto(x,y-3)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.penup()
turtle.goto(-50,-h/2-20)
turtle.pendown()
turtle.write("The point is "+status[1-inside]+" the rectangle")
turtle.hideturtle()
turtle.bye()



