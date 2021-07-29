# 7.1
class Rectangle:
    def __init__(self,width=1.0,height=1.0):
        self.__width=width
        self.__height=height

    def __getArea(self):
        return self.__width*self.__height

    def __getPerimeter(self):
        return 2*(self.__height+self.__width)

# 7.2
class Stock:
    def __init__(self,symbol,name,previousClosingPrice,currentPrice):
        self.symbol=symbol
        self.name=name
        self.previousClosingPrice=previousClosingPrice
        self.currentPrice=currentPrice

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getPreviousClosingPrice(self):
        return self.previousClosingPrice

    def setPreviousClosingPrice(self,pnewPrice):
        self.previousClosingPrice=pnewPrice

    def getCurrentPrice(self):
        return self.currentPrice

    def setCurrentPrice(self,cnewPrice):
        self.currentPrice=cnewPrice

    def getChangePercent(self):
        changePercent=(self.currentPrice-
        self.previousClosingPrice)/(self.previousClosingPrice)
        return changePercent

# 7.3
class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate

    # id
    def getId(self):
        return self.__id

    def setId(self,newId):
        self.__id=newId
    # balance
    def getBalance(self):
        return self.__balance

    def setBalance(self,newBalance):
        self.__balance=newBalance
    # rate
    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self,newRate):
        self.__annualInterestRate=newRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate/12

    def getMonthlyInterest(self):
        return self.__balance*self.getMonthlyInterestRate()

    def withdraw(self,amount1):
        self.__balance -= amount1
        # self.setBalance(self.__balance+amount1)

    def deposit(self,amount2):
        self.__balance += amount2
        # self.setBalance(self.__balance+amount2)


# 7.4
class Fan:
    SLOW,MEDIUM,FAST=1,2,3
    def __init__(self,speed=SLOW,on=False,radius=5.0,color="blue"):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color

    def getSpeed(self):
        return self.__speed
    def setSpeed(self,newSpeed):
        self.__speef=newSpeed

    def getOn(self):
        return self.__on
    def setOn(self,newOn):
        self.__on=newOn

    def getRadius(self):
        return self.__radius
    def setRadius(self,newRadius):
        self.__radius=newRadius

    def getColor(self):
        return self.__color
    def setColor(self,newColor):
        self.__color=newColor

# 7.6
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def getA(self):
        return self.__a
    def setA(self,newA):
        self.__a=newA

    def getB(self):
        return self.__b
    def setB(self,newB):
        self.__b=newB

    def getC(self):
        return self.__c
    def setC(self,newC):
        self.__c=newC

    def getD(self):
        return self.__d
    def setD(self,newD):
        self.__d=newD

    def getE(self):
        return self.__e
    def setE(self,newE):
        self.__e=newE

    def getF(self):
        return self.__f
    def setF(self,newF):
        self.__f=newF

    def isSolvable(self):
        judge=self.__a*self.__d-self.__b*self.__c
        return judge!=0

    def getX(self):
        x=(self.__e*self.__d-self.__b*self.__f)/\
        (self.__a*self.__d-self.__b*self.__c)
        return x

    def getY(self):
        y=(self.__a*self.__f-self.__e*self.__c)/ \
          (self.__a*self.__d-self.__b*self.__c)
        return y

# 7.9
class Linecross(LinearEquation):
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        a=y1-y2
        b=x2-x1
        c=y3-y4
        d=x4-x3
        e=x2*y1-x1*y2
        f=x4*y3-x3*y4
        super().__init__(a,b,c,d,e,f)
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        self.__x3=x3
        self.__y3=y3
        self.__x4=x4
        self.__y4=y4

    def getX1(self):
        return self.__x1
    def setX1(self,newX1):
        self.__x1=newX1

    def getY1(self):
        return self.__y1
    def setY1(self,newY1):
        self.__y1=newY1

    def getX2(self):
        return self.__x2
    def setX2(self,newX2):
        self.__x1=newX2

    def getY2(self):
        return self.__y2
    def setY2(self,newY2):
        self.__y2=newY2

    def getX3(self):
        return self.__x3
    def setX3(self,newX3):
        self.__x3=newX3

    def getY3(self):
        return self.__y3
    def setY3(self,newY3):
        self.__y3=newY3

    def getX4(self):
        return self.__x4
    def setX4(self,newX4):
        self.__x4=newX4

    def getY4(self):
        return self.__y4
    def setY4(self,newY4):
        self.__y4=newY4

    def intersectPoint(self):
        if self.isSolvable():
            return self.getX(), self.getY()
        else:
            return None

# 7.8
import time
class StopWatch:
    def __init__(self,startTime=0,endTime=0):
        self.__startTime=startTime
        self.__endTime=endTime

    def getStartTime(self):
        return self.__startTime
    def start(self):
        self.__startTime=time.time()

    def getEndTime(self):
        return self.__endTime
    def stop(self):
        self.__endTime=time.time()

    def getElapsedTime(self):
        delta=self.getEndTime() - self.getStartTime()
        return delta











