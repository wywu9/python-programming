# 二分查找
def binarySearch(lst,aimNumber):
    length=len(lst)
    high=length-1
    low=0
    while high>=low:
        middle=(high+low)//2
        if lst[middle]==aimNumber:
            return middle
        # 不能直接等于middle，会陷入死循环，找不到
        elif lst[middle]>aimNumber:
            high=middle-1
        elif lst[middle]<aimNumber:
            low=middle+1

    return -1


listTest=[2,4,7,10,11,45,50,59,60,66,69,70,79]
testNumber=45
binarySearch(listTest,testNumber)

# 选择排序
def selectionSort(lst):
    for i in range(len(lst)):
        currentMin=lst[i]
        currenMinIndex=i

        for j in range(i+1,len(lst)):
            if lst[j]<currentMin:
                currentMin=lst[j]
                currenMinIndex=j

        if currenMinIndex!=i:
            lst[currenMinIndex]=lst[i]
            lst[i]=currentMin

    return lst

listTest=[1,9,4.5,10.6,5.7,-4.5]
selectionSort(listTest)


# 插入排序
def insertionSort(lst):
    for i in range(1,len(lst)):
        currentElement=lst[i]
        k=i-1
        while k>=0 and lst[k]>currentElement:
                lst[k+1]=lst[k]
                k-=1

        lst[k+1]=currentElement
    return lst
listTest=[1,9,4.5,10.6,5.7,-4.5]
insertionSort(listTest)

# Bounce Ball
from tkinter import *
from random import randint

class Ball:
    def __init__(self):
        self.x=0
        self.y=0
        self.dx=2
        self.dy=2
        self.radius=3
        self.color=getRandomColor()

class BounceBalls:
    def __init__(self):
        window=Tk()
        window.title("Bouncing Balls")
        self.width=350
        self.height=150

        self.canvas=Canvas(window,width=self.width,height=self.height,bg="white")
        self.canvas.pack()

        frame1=Frame(window)
        frame1.pack()

        btStop=Button(frame1,text="Stop",command=self.stop)
        btStop.pack(side=LEFT)
        btResume=Button(frame1,text="Resume",command=self.resume)
        btResume.pack(side=LEFT)
        btAdd=Button(frame1,text='+',command=self.add)
        btAdd.pack(side=LEFT)
        btReduce=Button(frame1,text='-',command=self.reduce)
        btReduce.pack(side=LEFT)

        self.isStopped=False
        self.ballList=[]
        self.sleepTime=100 # ms
        self.animate()

        window.mainloop()


    def stop(self):
        self.isStopped=True

    def resume(self):
        self.isStopped=False
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def reduce(self):
        self.ballList.pop()

    def animate(self):
        # 这里是while循环保证持续运动到边界，而不是if判断！
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("Ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

    def redisplayBall(self,ball):
        if ball.x==self.width or ball.x<0:
            ball.dx= -ball.dx
        elif ball.y==self.height or ball.y<0:
            ball.dy= -ball.dy
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x-ball.radius,ball.y-ball.radius,
            ball.x+ball.radius,ball.y+ball.radius,fill=ball.color,tags="Ball")

def getRandomColor():
    # a random color: #RRGGBB
    color="#"
    for i in range(6):
        color+=toHexChar(randint(0,15))
    return color

def toHexChar(number):
    if 0<=number<=9:
        return chr(number+ord('0'))
    else:
        return chr(number-10+ord('A'))

BounceBalls()

# 10.1
def findBest(scoreList):
    best=0
    for score in scoreList:
        score=int(score)
        if score>best:
            best=score
    return best

def rank(best,score):
    rank=''
    if score>=best-10:
        rank='A'
    elif score>=best-20:
        rank='B'
    elif score>=best-30:
        rank='C'
    elif score>=best-40:
        rank='D'
    else:
        rank='F'
    return rank

scoreString=input("Enter scores:")
scoreList=scoreString.split(' ')

best=findBest(scoreList)
for i in range(len(scoreList)):
    print("Student ",i," score is ",scoreList[i],
          " and grade is ",rank(best,int(scoreList[i])))

# 10.2
integerListString=input("Enter integers between 1 and 100:").split(' ')
length=len(integerListString)
for i in range(length):
    print(integerListString.pop(),end=' ')

# 10.3
timesList=[0]*100
integers=input("Enter integers between 1 and 100:").split()
timePlural=["time","times"]
for i in range(len(integers)):
    integer=int(integers[i])
    timesList[integer-1] += 1
for i in range(100):
    if timesList[i]!=0:
        print(i+1,"occurs ",timesList[i]," ",timePlural[timesList[i]-1>0])

# 10.4
def mean(numberList):
    summary=0
    for number in numberList:
        summary += number
    return summary/len(numberList)
scoreString=input("Enter scores:").split(' ')
scoreList=[]
scoreList.extend(int(score) for score in scoreString)
higher,lower=0,0
scorePlural=[" score is"," scores are"]
for score in scoreList:
    if score>mean(scoreList):
        higher += 1
    elif score<mean(scoreList):
        lower += 1
print(higher,scorePlural[higher-1>0],"higher than mean, and ",lower,
      scorePlural[lower-1>0],"lower than mean.")

# 10.5
numberString=input("Enter ten numbers:").split(' ')
numberList,distinctList=[],[]
numberList.extend(int(number) for number in numberString)
print("The distinct numbers are: ",end='')
for number in numberList:
    if number not in distinctList:
        distinctList.append(number)
        print(number,end=' ')

# 10.7
from random import randint
counts=[0]*10
randomList=[randint(0,9) for i in range(1000)]
for number in randomList:
    counts[number] += 1
print(counts)

# 10.8
def indexOfSmallElement(lst):
    min=lst[0]
    for number in lst:
        if min>number:
            min=number
    return lst.index(min)
numberString=input("Enter numbers:").split(' ')
numberList=[int(number) for number in numberString]
print(indexOfSmallElement(numberList))

# 10.9
def mean(numberList):
    summary=0
    for number in numberList:
        summary += number
    return summary/len(numberList)

def deviation(numberList):
    deviation0=0
    mean0=mean(numberList)
    for number in numberList:
        deviation0 += (number-mean0)**2
    deviation0=(deviation0/(len(numberList)-1))**0.5
    return deviation0
numberString=input("Enter numbers:").split(' ')
numberList=[float(number) for number in numberString]
print("The mean is ",format(mean(numberList),'.2f'))
print("The standard deviation is ",format(deviation(numberList),'.5f'))

# 10.11
from random import randint
def shuffle(lst):
    length=len(lst)
    for i in range(len(lst)):
        index1=randint(0,length-1)
        index2=randint(0,length-1)
        lst[index1],lst[index2]=lst[index2],lst[index1]
    return lst
numberString=input("Enter numbers:").split(' ')
numberList=[float(number) for number in numberString]
shuffle(numberList)

# 10.12
def min(numberList):
    minNumber=numberList[0]
    for number in numberList:
        if number<minNumber:
            minNumber=number
    return minNumber

def gcd(numbersList):
    gcdNumber=0
    for i in range(1,min(numberList)+1):
        gcdFlag=True # 需要放在循环内部
        for number in numberList:
            if number%i!=0:
                gcdFlag=False
                break
        if gcdFlag==True:
            gcdNumber=i
    return gcdNumber
numberString=input("Enter numbers:").split(' ')
numberList=[int(number) for number in numberString]
print(gcd(numberList))

# 10.14
def selectSortExtend(lst):
    for i in range(len(lst)-1,-1,-1):
        currentMaxIndex=i
        currentMax=lst[i]
        for j in range(i-1,-1,-1):
            if lst[j]>currentMax:
                currentMax=lst[j]
                currentMaxIndex=j
        if currentMaxIndex!=i:
            lst[i],lst[currentMaxIndex]=lst[currentMaxIndex],lst[i]
    return lst

numberString=input("Enter numbers:").split(' ')
numberList=[int(number) for number in numberString]
print(selectSortExtend(numberList))

# 10.15
def isSorted(lst):
    ifSorted=True
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            ifSorted=False
            break

    if ifSorted:
        print("The list is already sorted")
    else:
        print("The list is not sorted")

numberString=input("Enter numbers:").split(' ')
numberList=[int(number) for number in numberString]
isSorted(numberList)

# 10.16
def bubbleSort(lst):
    isSorted=False
    while not isSorted:
        count=0
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                count+=1
        if count:
            isSorted=False
        else:
            isSorted=True
    return lst

numberString=input("Enter numbers:").split(' ')
numberList=[int(number) for number in numberString]
bubbleSort(numberList)

# 10.17
def isAnagram(s1,s2):
    isLike=True
    if len(s1)!=len(s2):
        isLike=False
    else:
        for char in s1:
            if char not in s2:
                isLike=False
    return isLike

string1=input("Enter string1:")
string2=input("Enter string1:")
if isAnagram(string1,string2):
    print("is an anagram")
else:
    print("is not an anagram")

# 10.18 BUG
#
def Queen(row):
    if row>7:
        return
    for column in range(8):
        if isLegal(row,column):
            queen[row][column]=1
            Queen(row+1)
            queen[row][column]=0


def isLegal(row,column):
    # row and column
    for i in range(row-1):
        if queen[i][column]==1:
            return False
    for j in range(8):
        if j !=column and queen[row][j]==1:
            return False

    for i in range(row-1):
        for j in range(8):
            if queen[i][j]==1 and abs(column-j)==(row-i):
                return False
    return True


def printMap(xList,yList):
    queenCounter=0
    for i in range(8):
        for j in range(8):
            if queenCounter<8 and i==xList[queenCounter] \
                    and j==yList[queenCounter]:
                print('|Q',end='')
                queenCounter+=1
            else:
                print('| ',end='')
            if j==7:
                print('|')

global queen
queen=[]
# 二维列表
for i in range(8):
    queen.append([0]*8)
for row in range(8):
    Queen(row)
print(queen)




























