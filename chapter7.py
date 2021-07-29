# 7.1
from chapter7_class import Rectangle
rec0=Rectangle()
rec1=Rectangle(4,40)
rec2=Rectangle(3.5,35.7)
print("rect",'\t','area','\t','perimeter')
for i in range(3):
    print('rect'+str(i),'\t',
        # 为什么还要加上前缀 _Rectangle？ 私有数据域的不同
        eval('rec'+str(i)+'.'+'_Rectangle__getArea()'),'\t',
        eval('rec'+str(i)+'.'+'_Rectangle__getPerimeter()'),end='\n')

# 7.2
from chapter7_class import Stock
symbol="INTC"
name="Intel Corporation"
pClosingPrice=20.5
currentPrice=20.35
stockTest=Stock(symbol,name,pClosingPrice,currentPrice)
print(format(stockTest.getChangePercent(),'.2%'))

# 7.3
from chapter7_class import Account
id='1122'
balance=20000
annualRate=0.045
withdraw=2500
deposit=3000
accountTest=Account(id,balance,annualRate)
accountTest.withdraw(withdraw)
accountTest.deposit(deposit)
print(accountTest.getId(),' ',accountTest.getBalance(),' ',
      accountTest.getMonthlyInterestRate(),' ',
      accountTest.getMonthlyInterest())

# 7.4
from chapter7_class import Fan
SLOW,MEDIUM,FAST=1,2,3
fan0=Fan()
fan1=Fan(FAST,True,10,"yellow")
fan2=Fan(MEDIUM,False,5,"blue")
for i in range(3):
    print(eval('fan'+str(i)+'.'+'getSpeed()'),'\t',
          eval('fan'+str(i)+'.'+'getRadius()'),'\t',
          eval('fan'+str(i)+'.'+'getColor()'),'\t',
          eval('fan'+str(i)+'.'+'getOn()'))

# 7.6
from chapter7_class import LinearEquation
a,b,c,d,e,f=eval(input("Enter the six parameters of the equation:"))
linearEquation=LinearEquation(a,b,c,d,e,f)
if linearEquation.isSolvable():
    print('x=',linearEquation.getX(),' and y=',LinearEquation.getY())
else:
    print("This function has no solution.")

# 7.9
from chapter7_class import LinearEquation,Linecross
x1,y1,x2,y2=eval(input("Enter the endpoints of the first segment:"))
x3,y3,x4,y4=eval(input("Enter the endpoints of the second segment:"))
crossTest=Linecross(x1, y1, x2, y2, x3, y3, x4, y4)
if crossTest.intersectPoint()==None:
    print("The two lines have no intersecting point.")
else:
    x,y=crossTest.intersectPoint()
    print("The intersecting point is (",x,',',y,')')

# 7.8
from chapter7_class import StopWatch
watchTest=StopWatch()
watchTest.start()
summary=0
for i in range(1,10**6+1):
    summary += i
watchTest.stop()
watchTest.getElapsedTime()

