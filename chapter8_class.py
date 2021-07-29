
# 8.2
def find(s1,s2):
    if len(s1)>len(s2):
        return False
    else:
        for i in range(len(s2)-len(s1)+1):
            if s1==s2[i:len(s1)+i]:
                return True
        return False

# 8.4
def count(s,ch):
    counter=0
    for i in range(len(s)):
        if s[i]==ch:
            counter += 1
    return counter

# 8.5
def countString(s1,s2):
    counter=0
    step=0
    while step <= len(s1)-len(s2)+1:
        if s2==s1[step:step+len(s2)]:
            counter += 1
            step += len(s2)
        else:
            step += 1
    return counter

# 8.7
def getNumber(uppercaseLetter):
    number=uppercaseLetter.lower()
    numPool=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    for i in range(len(number)):
        if number[i].isalpha():
            for j in range(8):
                if number[i] in numPool[j]:
                    print(j+2,end='')
                    break
        else:
            print(number[i],end='')

# 8.8
def binaryToDecimal(binaryString):
    decimal=0
    for i in range(len(binaryString)):
        decimal=decimal*2+int(binaryString[i])
    return decimal

# 8.9
def binaryToHex(binaryValue):
    hex=''
    while binaryValue>0:
        counter=0
        hexByte=0
        while counter<4:
            hexByte=hexByte +binaryValue%10*2**counter
            binaryValue //= 10
            counter+=1
        if hexByte >=10:
            hex=chr(hexByte-10+ord('A'))+hex
        else:
            hex=str(hexByte)+hex
    return hex

# 8.10
def decimalToBinary(value):
    binaryNumber=''
    while value>0:
        binaryNumber=str(value%2)+binaryNumber
        value //= 2
    return int(binaryNumber)

# 8.11
def reverse(s):
    rString=''
    for i in range(len(s)):
        rString=s[i]+rString
    return rString

# 8.12
def geneSearcher(genomeString):
    start="ATG"
    end=["TAG","TAA","TGA"]
    genePool=[]
    step=0
    while step < len(genomeString)-2:
        if genomeString[step:step+3] == start:
            geneFragment=''
            step+=3
            while genomeString[step:step+3] not in end:
                geneFragment=geneFragment+genomeString[step]
                step+=1
            genePool.append(geneFragment)
            step+=3
        else:
            step+=1
    if len(genePool)==0:
        return None
    else:
        return genePool

# 8.15
def verify(s):
    verifyNumber=0
    for i in range(len(s)):
        verifyNumber+=int(s[i])*(i+1)
    if verifyNumber%11==10:
        return 'X'
    else:
        return str(verifyNumber%11)

# 8.17
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distance(self,otherPoint):
        d=((self.__x-otherPoint.__x)**2+
           (self.__y-otherPoint.__y)**2)**0.5
        return d

    # p1 is a point class object
    def isNearBy(self,p1):
        if self.distance(p1)<5:
            return True
        else:
            return False

    def __str__(self):
        x=str(self.__x)
        y=str(self.__y)
        pointString='('+x+','+y+')'
        return pointString

# 8.18
import math
class Circle2D:
    def __init__(self,x=0,y=0,radius=0):
        self.__x=x
        self.__y=y
        self.__radius=radius

    def getX(self):
        return self.__x
    def setX(self,newX):
        self.__x=newX

    def getY(self):
        return self.__y
    def setY(self,newY):
        self.__y=newY

    def getRadius(self):
        return self.__radius
    def setRadius(self,newRadius):
        self.__radius=newRadius

    def getArea(self):
        return math.pi*self.__radius**2

    def getPerimeter(self):
        return 2*math.pi*self.__radius

    def containsPoint(self,x,y):
        if (self.__x-x)**2+(self.__y-y)**2<=self.__radius**2:
            return True
        else:
            return False

    def contains(self,circle1):
        if math.sqrt((self.__x-circle1.__x)**2+\
            (self.__y-circle1.__y)**2)<=self.__radius-circle1.__radius:
            return True
        else:
            return False

    def overlap(self,circle1):
        distance=math.sqrt((self.__x-circle1.__x)**2+ \
                           (self.__y-circle1.__y)**2)
        if distance<self.__radius + circle1.__radius and \
           distance>self.__radius-circle1.__radius:
            return True
        else:
            return False

    def __contains__(self,another):
        if another.contains(self):
            return True
        else:
            return False

    def __cmp__(self,circle1):
        # 返回值为1：本圆半径更大
        compare=self.__radius-circle1.__radius
        if compare>0:
            compare=1
        elif compare<0:
            compare=-1
        return compare

    # less than
    def __lt__(self,circle1):
        return self.__radius<circle1.__radius

    # less equal
    def __le__(self,circle1):
        return self.__radius<=circle1.__radius

    # equal
    def __eq__(self,circle1):
        return self.__radius==circle1.__radius

    # not equal
    def __ne__(self,circle1):
        return self.__radius!=circle1.__radius

    # greater than
    def __gt__(self,circle1):
        return self.__radius>circle1.__radius

    # greater equal
    def __ge__(self,circle1):
        return self.__radius>=circle1.__radius

# 8.19
class Rectangle2D:
    def __init__(self,x=0,y=0,width=0,height=0):
        self.__x=x
        self.__y=y
        self.__width=width
        self.__height=height

    def getX(self):
        return self.__x
    def setX(self,newX):
        self.__x=newX

    def getY(self):
        return self.__y
    def setY(self,newY):
        self.__y=newY

    def getWidth(self):
        return self.__width
    def setWidth(self,newWidth):
        self.__width=newWidth

    def getHeight(self):
        return self.__height
    def setHeight(self,newHeight):
        self.__height=newHeight

    def getArea(self):
        return self.__width*self.__height

    def getPerimeter(self):
        return 2*(self.__width+self.__height)

    def containsPoint(self,x,y):
        if abs(x-self.__x)<=self.__width/2 and \
            abs(y-self.__y)<=self.__height/2:
            return True
        else:
            return False

    def contain(self,rectangle):
        if abs(self.__x-rectangle.__x)<=(self.__width+rectangle.__width)/2 and \
           abs(self.__y-rectangle.__y)<=(self.__width-rectangle.__width)/2 and \
           self.__width>rectangle.__width and self.__height>rectangle.__height:
            return True
        else:
            return False

    def overlaps(self,rectangle):
        if abs(self.__x-rectangle.__x)<(self.__width+rectangle.__width)/2 and \
           abs(self.__x-rectangle.__x)>(self.__width-rectangle.__width)/2 and \
           abs(self.__y-rectangle.__y)<(self.__width+rectangle.__width)/2 and \
           abs(self.__y-rectangle.__y)>(self.__width-rectangle.__width)/2:
            return True
        else:
            return False

    def __contains__(self,another):
        if another.contains(self):
            return True
        else:
            return False

    # 返回值为1表明本矩形面积更大
    def __cmp__(self,rectangle):
        compare=self.getArea()-rectangle.getArea()
        if compare>0:
            compare=1
        else:
            compare=-1
        return compare

    def __lt__(self,rectangle):
        return self.getArea()<rectangle.getArea()

    def __le__(self,rectangle):
        return self.getArea()<=rectangle.getArea()

    def __eq__(self,rectangle):
        return self.getArea()==rectangle.getArea()

    def __ne__(self,rectangle):
        return self.getArea()!=rectangle.getArea()

    def __gt__(self,rectangle):
        return self.getArea()>rectangle.getArea()

    def __ge__(self,rectangle):
        return self.getArea()>=rectangle.getArea()

# 8.21
class Complex:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

    def __add__(self,complex1):
        newA=self.a+complex1.a
        newB=self.b+complex1.b
        return str(Complex(newA,newB))

    def __sub__(self,complex1):
        newA=self.a-complex1.a
        newB=self.b-complex1.b
        return str(Complex(newA,newB))

    def __mul__(self,complex1):
        newA=self.a*complex1.a-self.b*complex1.b
        newB=self.a*complex1.b+self.b*complex1.a
        return str(Complex(newA,newB))

    def __truediv__(self,complex1):
        newA=(self.a*complex1.a-self.b*complex1.b)/ \
                   (complex1.a**2+complex1.b**2)
        newB=(self.b*complex1.a-self.a*complex1.b)/ \
                   (complex1.a**2+complex1.b**2)
        return str(Complex(newA,newB))

    def __abs__(self):
        return (self.a**2+self.b**2)**0.5

    def __str__(self):
        if self.b==0:
            return str(self.a)
        else:
            if self.b>0:
                string='('+str(self.a)+' + '+str(self.b)+'i'+')'
            else:
                string='('+str(self.a)+str(self.b)+'i'+')'
            return string

    def getRealPart(self):
        return self.a

    def getImaginaryPart(self):
        return self.b






