# 8.1
ssn=input("Enter ddd-dd-dddd:")
ssn=ssn.strip()
judge=True
for i in range(len(ssn)):
    if i in [3,6]:
        judge=ssn[i]=='-'
    else:
        judge=ssn[i].isdigit()
    if judge==False:
        break
if judge:
    print("Valid SSN")
else:
    print("Invalid SSN")

# 8.2
from chapter8_class import find
string1=input("Enter the first string:")
string2=input("Enter the second string:")
if find(string1,string2):
    print("string1 is a substring of string2")
else:
    print("string1 is not a substring of string2")

# 8.3
password=input("Enter your password:")
digitCount=0
if len(password)>=8 and password.isalnum():
    for i in range(len(password)):
        if password[i].isdigit():
            digitCount += 1
            if digitCount>=2:
                break
    if digitCount>=2:
        print("valid password")
    else:
        print("invalid password")
else:
    print("invalid password")

# 8.4
from chapter8_class import count
string=input("Enter your string:")
char=input("Enter your char:")
count(string,char)

# 8.5
from chapter8_class import countString
string1=input("Enter your first string:")
string2=input("Enter your second string:")
countString(string1,string2)

# 8.7
from chapter8_class import getNumber
number=input("Enter a string:")
getNumber(number)

# 8.8
from chapter8_class import binaryToDecimal
binaryString=input("Enter a binary string:")
print("The decimal counterpart of binaryString ",
      binaryString," is ",binaryToDecimal(binaryString))

# 8.9
from chapter8_class import binaryToHex
binaryNumber=eval(input("Enter a binary number:"))
print("The hex counterpart of the binary number ",
      binaryNumber,"is ",binaryToHex(binaryNumber))

# 8.10
from chapter8_class import decimalToBinary
decimalNumber=eval(input("Enter a decimal number:"))
print("The binary counterpart of the decimal number ",
      decimalNumber,"is ",decimalToBinary(decimalNumber))

# 8.11
from chapter8_class import reverse
stringTest=input("Enter a string:")
print("The reverse string is ",reverse(stringTest))

# 8.12
# test string: TTATGTTTTAAGGATGGGGCGTTAGTT
from chapter8_class import geneSearcher
genomeString=input("Enter a genomeString:")
gene=geneSearcher(genomeString)
if gene==None:
    print("no gene is found")
else:
    for i in range(len(gene)):
        print(gene[i])

# 8.13
def main():
    string1=input("Enter the first string:")
    string2=input("Enter the second string:")
    print(prefix(string1,string2))

def prefix(s1,s2):
    sPrefix=''
    if len(s1)>len(s2):
        s1,s2=s2,s1
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            sPrefix=sPrefix+s1[i]
    return sPrefix

main()

# 8.15
from chapter8_class import verify
preISBN=input("Enter the first 9 digits "
              "of an ISBN-10 as a string:")
print("The ISBN-10 number is ",preISBN+verify(preISBN))

# 8.17
from chapter8_class import Point
x1,y1,x2,y2=eval(input("Enter two points x1,y1,x2,y2:"))
point1=Point(x1,y1)
point2=Point(x2,y2)
print("The distance between the two points is ",
      format(point1.distance(point2),".2f"))
if point1.isNearBy(point2):
    print("The two points are near each other")
else:
    print("The two points are not near each other")

# 8.18
from chapter8_class import Circle2D
x1,y1,radius1=eval(input("Enter x1,y1,radius1:"))
x2,y2,radius2=eval(input("Enter x2,y2,radius2:"))
c1=Circle2D(x1,y1,radius1)
c2=Circle2D(x2,y2,radius2)
print("Area for c1 is ",c1.getArea())
print("Perimeter for c1 is ",c1.getPerimeter())
print("Area for c2 is ",c2.getArea())
print("Perimeter for c2 is ",c2.getPerimeter())
print("c1 contains the center of c2? ",c1.containsPoint(c2.getX(),c2.getY()))
print("c1 contains c2? ",c1.contains(c2))
# print("c2 is contained in c1? ",c1.__contains__(c2))
print("c1 overlaps c2? ",c1.overlap(c2))


# 8.19
from chapter8_class import Rectangle2D
x1,y1,width1,height1=eval(input("Enter x1,y1,width1,height1:"))
x2,y2,width2,height2=eval(input("Enter x2,y2,width2,height2:"))
r1=Rectangle2D(x1,y1,width1,height1)
r2=Rectangle2D(x2,y2,width2,height2)
print("Area for r1 is ",r1.getArea())
print("Perimeter for r1 is ",r1.getPerimeter())
print("Area for r2 is ",r2.getArea())
print("Perimeter for r2 is ",r2.getPerimeter())
print("r1 contains the center of r2?",
      r1.containsPoint(r2.getX(),r2.getY()))
print("r1 contains r2?",r1.contain(r2))
print("r1 overlaps r2?",r1.overlaps(r2))

# 8.21
from chapter8_class import Complex
a1,b1=eval(input("Enter the first complex number:"))
a2,b2=eval(input("Enter the second complex number:"))
c1=Complex(a1,b1)
c2=Complex(a2,b2)
print(str(c1),'+',str(c2),'=',str(c1.__add__(c2)))
print(str(c1),'-',str(c2),'=',str(c1.__sub__(c2)))
print(str(c1),'*',str(c2),'=',str(c1.__mul__(c2)))
print(str(c1),'/',str(c2),'=',str(c1.__truediv__(c2)))
print('|',str(c1),'|','=',abs(c1))


