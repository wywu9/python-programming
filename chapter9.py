# SimpleGUI
from tkinter import *

window=Tk()
label=Label(window,text="Welcome to Python")
button=Button(window,text="Click me")
label.pack()
button.pack()
window.mainloop()

# ProcessButtonEvent
from tkinter import *

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

window=Tk()
btOK=Button(window,text="OK",fg="red",
            command=processOK)
btCancel=Button(window,text="Cancel",bg="yellow",
                command=processCancel)

btOK.pack()
btCancel.pack()

window.mainloop()

# widgetsDemo
from tkinter import *
class WidgetsDemo:
    def __init__(self):
        window=Tk()
        window.title("Widgets Demo")
        frame1=Frame(window)
        frame1.pack()

        self.v1=IntVar()
        cbtBold=Checkbutton(frame1,text="Bold",
               variable=self.v1,command=self.processCheckbutton)

        self.v2=IntVar()
        rbRed=Radiobutton(frame1,text="Red",bg="red",
             variable=self.v2,value=1,
            command=self.processRadiobutton)
        rbYellow=Radiobutton(frame1,text="Yellow",
                bg="yellow",variable=self.v2,value=2,
                command=self.processRadiobutton)

        # 默认情况下将按钮置于网格中央
        cbtBold.grid(row=1,column=1)
        rbRed.grid(row=1,column=2)
        rbYellow.grid(row=1,column=3)

        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter your name:")
        self.name=StringVar()
        # 获取字符串形式的文本输入
        entryName=Entry(frame2,textvariable=self.name)
        btGetName=Button(frame2,text="Get Name",
                command=self.processButton)
        message=Message(frame2,text="It is a widgets demo")
        # 使用网格管理器把不同的button居中放置在不同的网格内
        label.grid(row=1,column=1)
        entryName.grid(row=1,column=2)
        btGetName.grid(row=1,column=3)
        message.grid(row=1,column=4)

        # 添加文本
        text=Text(window)
        text.pack()
        text.insert(END,
                    "Tip\nThe best way to learn Tkinter is to read")
        text.insert(END,
                    " these carefully designed examples and use them")
        text.insert(END," to create your applications")

        window.mainloop()

    def processCheckbutton(self):
        print("check button is "
              + ("checked" if self.v1.get()==1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get()==1 else "Yellow") + " is selected")

    def processButton(self):
        print("Your name is "+self.name.get())

WidgetsDemo()

# ChangeLabelDemo
from tkinter import *
class ChangeLabelDemo:
    def __init__(self):
        window=Tk()
        window.title("Change Label Demo")

        frame1=Frame(window)
        frame1.pack()
        self.lbl=Label(frame1,text="Programming is fun")
        self.lbl.pack()

        frame2=Frame(window)
        frame2.pack()
        label=Label(frame2,text="Enter text: ")
        self.msg=StringVar()
        entry=Entry(frame2,textvariable=self.msg)
        btChangeText=Button(frame2,text="Change Text",
            command=self.processButton)

        self.v1=StringVar()
        rbRed=Radiobutton(frame2,text="Red",bg="red",
                variable=self.v1,value='R',
                command=self.processRadiobutton)
        self.v2=StringVar()
        rbYellow=Radiobutton(frame2,text="Yellow",
            bg="yellow",variable=self.v2,value='Y',
                command=self.processRadiobutton)

        label.grid(row=1,column=1)
        entry.grid(row=1,column=2)
        btChangeText.grid(row=1,column=3)
        rbRed.grid(row=1,column=4)
        rbYellow.grid(row=1,column=5)

        window.mainloop()

    def processButton(self):
        if self.v1.get()=='R':
            self.lbl['fg']="red"
        elif self.v1.get()=='Y':
            self.lbl["fg"]="yellow"

    def processRadiobutton(self):
        self.lbl["text"]=self.msg.get()

ChangeLabelDemo()

# CanvasDemo
from tkinter import *
class CanvasDemo:
    def __init__(self):
        # create a window
        window=Tk()
        window.title("Canvas Demo")

        # place canvas in the window
        self.canvas=Canvas(window,width=200,
            height=100,bg='white')
        self.canvas.pack()

        # place buttons in frame
        frame=Frame(window)
        frame.pack()
        # bt-button 缩写
        btRectangle=Button(frame,text="Rectangle",
            command=self.displayRect)
        btOval=Button(frame,text="Oval",
            command=self.displayOval)
        btArc=Button(frame,text="Arc",
            command=self.displayArc)
        btPolygon=Button(frame,text="Polygon",
            command=self.displayPolygon)
        btLine=Button(frame,text="Line",
            command=self.displayLine)
        btString=Button(frame,text="String",
            command=self.displayString)
        btClear=Button(frame,text="Clear",
            command=self.clearCanvas)

        btRectangle.grid(row=1,column=1)
        btOval.grid(row=1,column=2)
        btArc.grid(row=1,column=3)
        btPolygon.grid(row=1,column=4)
        btLine.grid(row=1,column=5)
        btString.grid(row=1,column=6)
        btClear.grid(row=1,column=7)

        # 创建一个事件循环（event loop)
        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,90,tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10,10,190,90,fill="red",
                                tags="oval")

    def displayArc(self):
        self.canvas.create_arc(10,10,190,90,start=0,
            extent=90,width=8,fill="red",tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10,10,190,90,30,50,
                    tags="polygon")

    def displayLine(self):
        self.canvas.create_line(10,10,190,90,fill="red",
                                tags="line")
        self.canvas.create_line(10,90,190,10,width=9,
                                arrow="last",activefill="blue",tags="line")

    def displayString(self):
        self.canvas.create_text(60,40,text="Hi, I am a \
            string",font="Times 10 bold underline",tags="string")

    def clearCanvas(self):
        self.canvas.delete("rect","oval","arc","polygon",
            "line","string")

CanvasDemo()

# gridManagerDemo
from tkinter import *
class GridManagerDemo:
    window=Tk()
    window.title("Grid Manager Demo")

    message=Message(window,text=
    "This message widget occupies three rows and two columns")
    message.grid(row=1,column=1,rowspan=3,columnspan=2)
    Label(window,text="First Name:").grid(row=1,column=3)
    Entry(window).grid(row=1,column=4,padx=5,pady=5)
    Label(window).grid(row=2,column=3)
    Entry(window).grid(row=2,column=4)
    Button(window,text="Get Names").grid(row=3,
        padx=5,pady=5,column=4,sticky=E)

    window.mainloop()


GridManagerDemo()

# PackManagerDemo
from tkinter import *
class PackManagerDemo:
    def __init__(self):
        window=Tk()
        window.title("Pack Manager Demo 1")

        Label(window,text="blue",bg="blue").pack()
        Label(window,text="red",bg="red").pack(
                fill=BOTH,expand=1)
        Label(window,text="Green",bg="green").pack(
                fill=BOTH)

        window.mainloop()

PackManagerDemo()

# PackManagerDemoWithSide
from tkinter import *
class PackManagerDemoWithSide:
    window=Tk()
    window.title("Pack Manager Demo 2")

    Label(window,text="Blue",bg="blue").pack(side=LEFT)
    Label(window,text="Red",bg="red").pack(side=LEFT,
          fill=BOTH)
    Label(window,text="Green",bg="green").pack(side=LEFT,
          fill=BOTH)

    window.mainloop()

PackManagerDemoWithSide()

# PlaceManagerDemo
from tkinter import *

class PlaceManagerDemo:
    def __init__(self):
        window=Tk()
        window.title("Place Manager Demo")

        Label(window,text="Blue",bg="blue").\
            place(x=20,y=20)
        Label(window,text="Red",bg="red").place(
            x=50,y=50)
        Label(window,text="Green",bg="green").place(
            x=80,y=90)

        window.mainloop()

PlaceManagerDemo()

# 9.1
from tkinter import *
RADIUS=20
STEP=40
WIDTH=400
HEIGHT=300
class MovingBall:
    def __init__(self):
        window=Tk()
        window.title("Moving Ball")

        self.canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
        self.canvas.pack()

        self.xStart=WIDTH/2-RADIUS
        self.yStart=HEIGHT/2-RADIUS
        self.xEnd=WIDTH/2+RADIUS
        self.yEnd=HEIGHT/2+RADIUS

        self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,
                                fill="red",tags="oval")

        frame1=Frame(window)
        frame1.pack()

        btLeft=Button(frame1,text="Left",command=self.MovingLeft)
        btRight=Button(frame1,text="Right",command=self.MovingRight)
        btUp=Button(frame1,text="Up",command=self.MovingUp)
        btDown=Button(frame1,text="Down",command=self.MovingDown)
        btLeft.grid(row=1,column=1)
        btRight.grid(row=1,column=2)
        btUp.grid(row=1,column=3)
        btDown.grid(row=1,column=4)

        window.mainloop()


    def MovingLeft(self):
        self.canvas.delete("oval")
        if self.xStart>0:
            self.xStart -= STEP
            self.xEnd -= STEP
        else:
            self.xStart=WIDTH+self.xStart
            self.xEnd=self.xStart+2*RADIUS
        self.canvas.update()
        self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,
                                fill="red",tags="oval")

    def MovingRight(self):
        self.canvas.delete("oval")
        if self.xEnd<WIDTH:
            self.xStart += STEP
            self.xEnd += STEP
        else:
            self.xEnd=self.xEnd-WIDTH
            self.xStart=self.xEnd-2*RADIUS
        self.canvas.update()
        self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,
                                fill="red",tags="oval")

    def MovingUp(self):
        self.canvas.delete("oval")
        if self.yStart>0:
            self.yStart -= STEP
            self.yEnd -= STEP
        else:
            self.yStart=HEIGHT+self.yStart
            self.yEnd=self.yStart+2*RADIUS
        self.canvas.update()
        self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,
                                fill="red",tags="oval")

    def MovingDown(self):
        self.canvas.delete("oval")
        if self.yEnd<HEIGHT:
            self.yStart += STEP
            self.yEnd += STEP
        else:
            self.yEnd=self.yEnd-HEIGHT
            self.yStart=self.yEnd-2*RADIUS
        self.canvas.update()
        self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,
                                fill="red",tags="oval")


MovingBall()

# 9.2
from tkinter import *
class InvestmentCalculator:
    def __init__(self):
        window=Tk()
        window.title("Investment Calculator")

        Label(window,text="Investment Amount").grid(row=1,column=1,sticky=W)
        Label(window,text="Years").grid(row=2,column=1,sticky=W)
        Label(window,text="Annual Interest Rate").grid(row=3,column=1,sticky=W)
        Label(window,text="Future Value").grid(row=4,column=1,sticky=W)

        self.amount=StringVar()
        Entry(window,textvariable=self.amount,justify=RIGHT).grid(row=1,column=3)

        self.year=StringVar()
        Entry(window,textvariable=self.year,justify=RIGHT).grid(row=2,column=3)

        self.annualRate=StringVar()
        Entry(window,textvariable=self.annualRate,justify=RIGHT).grid(row=3,column=3)

        self.futureValue=StringVar()
        Label(window,textvariable=self.futureValue).\
           grid(row=4,column=3,sticky=E)

        Button(window,text="Calculate",command=self.CalculateInvestment).\
            grid(row=5,column=3,sticky=E)

        window.mainloop()

    def CalculateInvestment(self):
        value=float(self.amount.get())*(1+
            float(self.annualRate.get())/1200)**(int(self.year.get())*12)
        self.futureValue.set(format(value,"10.2f"))


InvestmentCalculator()


# 9.3
from tkinter import *
WIDTH=200
HEIGHT=100

class DrawRecOval:
    def __init__(self):
        window=Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
        self.canvas.pack()
        self.state=''

        frame1=Frame(window)
        frame1.pack()
        # value标识不同的选项，不同的radiobutton对应的value不能相同，但是作为同一变量的不同值存在的
        self.shape=IntVar()
        Radiobutton(frame1,text="Rectangle",variable=self.shape,value=1,
           command=self.displayRectangle).grid(row=1,column=1)
        Radiobutton(frame1,text="Oval",variable=self.shape,value=2,
           command=self.displayOval).grid(row=1,column=2)

        self.fill=BooleanVar()
        Checkbutton(frame1,text="Filled",variable=self.fill,
                   command=self.fillColor ).grid(row=1,column=3)

        window.mainloop()

    def displayRectangle(self):
        if len(self.state)!=0: self.clearCanvas(self.state)
        if self.fill.get():
            self.fillColor()
        else:
            self.canvas.create_rectangle(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2,tags="rectangle")
            self.state="rectangle"

    def displayOval(self):
        if len(self.state)!=0: self.clearCanvas(self.state)
        if self.fill.get():
            self.fillColor()
        else:
            self.canvas.create_oval(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2,tags="oval")
            self.state="oval"

    def fillColor(self):
        if len(self.state)!=0:
            self.clearCanvas(self.state)
        if self.fill.get():
            if self.shape.get()==1:
                self.canvas.create_rectangle(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2,fill="blue",
                                     tags="colorRect")
                self.state="colorRect"
            else:
                self.canvas.create_oval(WIDTH/4,HEIGHT/4,WIDTH/2,HEIGHT/2,fill="blue",
                            tags="colorOval")
                self.state="colorOval"
        else:
            if self.shape.get()==1:
                self.displayRectangle()
            else:
                self.displayOval()


    def clearCanvas(self,shape):
        self.canvas.delete(shape)


DrawRecOval()

# 9.4
from tkinter import *

WIDTH=500
HEIGHT=300
STEP=8
COUNTER=20

window=Tk()
window.title("Display Rectangle")

canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
canvas.pack()

for i in range(COUNTER):
    xStart=i*STEP
    yStart=i*STEP
    xEnd=xStart+WIDTH-2*i*STEP
    yEnd=yStart+HEIGHT-2*i*STEP
    canvas.create_rectangle(xStart,yStart,
            xEnd,yEnd)

window.mainloop()

# 9.5
from tkinter import *
WIDTH=400
HEIGHT=400
SIDE=50
COUNTER=8

window=Tk()
window.title("Displaying a Checkboard")

canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")
canvas.pack()
listEven=[0,2,4,6]
listOdd=[1,3,5,7]

for i in range(COUNTER):
    for j in range(COUNTER):
        xStart=SIDE*i
        yStart=SIDE*j
        xEnd=xStart+SIDE
        yEnd=yStart+SIDE
        if (i in listEven and j in listEven) or \
            (i in listOdd and j in listOdd):
            canvas.create_rectangle(xStart,yStart,
                   xEnd,yEnd,fill="white")
        else:
            canvas.create_rectangle(xStart,yStart,
                   xEnd,yEnd,fill="black")

window.mainloop()

# 9.6
from tkinter import *
from random import randint

class WellImage:
    def __init__(self):
        window=Tk()
        window.title("Well Image")
        # create image object
        heartImage=PhotoImage(file="image/heart.gif")
        circleImage=PhotoImage(file="image/circle.gif")
        imagePool=[heartImage,circleImage]

        for i in range(3):
            for j in range(3):
                imageSign=randint(0,1)
                Label(window,image=imagePool[imageSign]).grid(row=i+1,column=j+1)
        # mainloop()要与canvas,photoimage在同一作用域下
        window.mainloop()

WellImage()

# 9.7 BUG
from tkinter import *
WIDTH=160
HEIGHT=160
SIDE=20
window=Tk()
window.title("Grid")
canvas=Canvas(window,width=WIDTH,height=HEIGHT,bg="white")

for i in range(7):
        # vertical
        xStart=i*SIDE+SIDE
        yStart=0
        xEnd=xStart
        yEnd=yStart+HEIGHT
        canvas.create_line(xStart,yStart,xEnd,yEnd,fill="red",tags="line")

        # horizontal
        xStart=0
        yStart=i*SIDE+SIDE
        xEnd=xStart+WIDTH
        yEnd=yStart
        canvas.create_line(xStart,yStart,xEnd,yEnd,fill="blue",tags="line")

window.mainloop()






















