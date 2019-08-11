from turtle import *
from random import randint as r,choice as ch
sc=Screen()
sc.tracer(1000,0)
sc.bgcolor("white")
sc.setup(800, 800)
#sc.screensize(1920, 1080)

class game():
    def __init__(self):
        global kill
        self.sc=Screen()
        self.t=[]
        self.bullet=[]
        self.Superbullet=[]
        self.monsterbullet=[]
        for c in range(8):
            tom=Turtle()
            tom.ht()
            tom.color("blue")
            self.t.append(tom)

        self.t[2].penup()
        self.t[2].color("red")
        self.t[2].goto(-350,-300)
        self.t[2].pendown()
        self.t[2].goto(350,-300)
        self.t[2].goto(350,300)
        self.t[2].goto(-350,300)
        self.t[2].goto(-350,-300)
        for c in range(3):
            self.t[3+c].penup()
            self.t[3+c].color("red")
            self.t[3+c].goto(-350+(c*300),-350)
        self.Elive=10
        self.live=5
        self.score=0
        self.t[3].write("Enemy Live:%s"%self.Elive,0,"left",("Arial", 30, "normal"))
        self.t[4].write("Kill:%s"%kill,0,"left",("Arial", 30, "normal"))
        self.t[5].color("green")
        self.t[5].write("Live:%s"%self.live,0,"left",("Arial", 30, "normal"))
        self.sc.listen()
        self.Eyspeed=0
        self.Exspeed=0
        self.LRC=ch([-1,1])
        self.LRR=0
        self.x=0
        self.y=0
        self.xt=0
        self.yt=0
        self.shooting=False
        self.TFC=False
        self.PC=0
        self.countB=0
        self.countSB=0
        self.countMSB=0
        self.left()
        self.right()
     
    def LV1(self,turtle,x,y,h):
        turtle.clear()
        turtle.seth(h)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for c in range(4):
            turtle.forward(30)
            turtle.left(90)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        for c in range(5):
            for c in range(3):
                turtle.forward(10)
                turtle.right(120)
            turtle.forward(5)
        turtle.backward(25)
        turtle.left(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.pu()
        turtle.forward(5)
        turtle.pd()
        for c in range(2):
            turtle.forward(20)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
        turtle.forward(6)
        turtle.begin_fill()
        for c in range(2):
            turtle.forward(8)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()

    def monstermove(self,fun,turtle):
        self.Eyspeed+=0.5
        self.Exspeed+=5*self.LRC
     
        y=270-self.Eyspeed
        if turtle.xcor()+15<335 and turtle.xcor()>-335:
            x=self.LRR+self.Exspeed
        else:
            self.Exspeed=0
            self.LRR=r(-335,335)
            self.LRC=ch([-1,1])
            self.Exspeed+=r(0,5)*self.LRC
            x=self.LRR+self.Exspeed
        if turtle.ycor()<-300:
            self.Eyspeed=0
        fun(turtle,x,y,0)
        self.sc.update()

    def monstershoot(self):
        if 100==r(-50,150):
            _=Turtle()
            _.shape("square")
            _.shapesize(0.2,0.4)
            _.color("red")
            _.penup()
            _.goto(self.t[6].xcor()+15,self.t[6].ycor()+15)
            _.setheading(_.towards(self.x,self.y))
            self.monsterbullet.append(_)
            self.countMSB+=1
            
        self.sc.update()
        
        
     
    def cat(self,x=None,y=None,h=0,l=0.5):
        self.t[0].clear()
        self.t[0].seth(h)
        self.t[0].penup()
        self.t[0].goto(x,y)
        self.t[0].pendown()
     
        self.t[0].forward(100*l)
        self.t[0].left(90)
        self.t[0].forward(70*l)
        self.t[0].left(90)
        self.t[0].forward(30*l)
        self.t[0].left(90)
        self.t[0].forward(20*l)
        self.t[0].right(90)
        self.t[0].forward(40*l)
        self.t[0].right(90)
        self.t[0].forward(10*l)
        self.t[0].left(90)
        self.t[0].forward(30*l)
        self.t[0].left(90)
        self.t[0].forward(60*l)

        self.t[0].backward(40*l)
        self.t[0].left(90)
        self.t[0].forward(40*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        for c in range(2):
            self.t[0].forward(10*l)
            self.t[0].right(90)
            self.t[0].forward(30*l)
            self.t[0].right(90)
        self.t[0].forward(15*l)
        self.t[0].left(90)
        self.t[0].forward(5*l)
        self.t[0].right(90)
     
        self.t[0].forward(10*l)
        self.t[0].right(90)
        self.t[0].forward(20*l)
        self.t[0].right(90)
        self.t[0].forward(10*l)
        self.t[0].backward(4*l)
        self.t[0].left(80)
        self.t[0].forward(30*l)
        self.t[0].backward(30*l)
        self.t[0].left(100)
        self.t[0].forward(4*l)
        self.t[0].right(80)
        self.t[0].forward(30*l)
        self.t[0].backward(30*l)
        self.t[0].left(80)
        self.t[0].forward(2*l)
        self.t[0].left(90)
        self.t[0].forward(20*l)
        self.t[0].left(90)
        self.t[0].forward(2*l)

        self.t[0].right(90)
        self.t[0].forward(30*l)
        self.t[0].left(90)
        self.t[0].forward(10*l)
        self.t[0].backward(4*l)
        self.t[0].right(80)
        self.t[0].forward(30*l)
        self.t[0].backward(30*l)
        self.t[0].right(100)
        self.t[0].forward(4*l)
        self.t[0].left(80)
        self.t[0].forward(30*l)
        self.t[0].backward(30*l)
        self.t[0].right(80)
        self.t[0].forward(2*l)
        self.t[0].right(90)
        self.t[0].forward(30*l)

        self.t[0].right(90)
        self.t[0].forward(8*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].left(90)
        self.t[0].forward(5*l)
        for c in range(2):
            self.t[0].forward(10*l)
            self.t[0].right(90)
            self.t[0].forward(30*l)
            self.t[0].right(90)
        self.t[0].forward(15*l)
        self.t[0].right(90)
        self.t[0].forward(50*l)

        self.t[0].right(90)
        self.t[0].forward(20*l)
        self.t[0].left(90)
        self.t[0].forward(200*l)
        self.t[0].right(90)
        for c in range(2):
            self.t[0].forward(15*l)
            self.t[0].right(90)
            for i in range(2):
                self.t[0].forward(10*l)
                self.t[0].backward(5*l)
                for i in range(2):
                    self.t[0].forward(5*l)
                    self.t[0].right(90)
                    self.t[0].forward((15*(c+1))*l)
                    self.t[0].backward((15*(c+1))*l)
                    self.t[0].left(90)
            self.t[0].left(90)
        self.t[0].forward(20*l)
        self.t[0].right(90)
        self.t[0].forward(40*l)
     
        self.t[0].left(90)
        self.t[0].forward(25*l)
        self.t[0].right(90)
        self.t[0].forward(7*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].backward(5*l)
        self.t[0].left(90)
        self.t[0].forward(6*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].backward(5*l)
        self.t[0].left(90)
        self.t[0].forward(7*l)
        self.t[0].right(90)
        self.t[0].forward(25*l)
        self.t[0].left(90)
        self.t[0].forward(5*l)
     
        self.t[0].left(90)
        self.t[0].forward(20*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].backward(5*l)
        self.t[0].left(90)
        self.t[0].forward(5*l)
        self.t[0].right(90)
        self.t[0].forward(5*l)
        self.t[0].backward(5*l)
        self.t[0].left(90)
        self.t[0].forward(5*l)
        self.t[0].right(90)
        for c in range(3):
            self.t[0].forward(20*l)
            self.t[0].right(90)
            self.t[0].forward(15*l)
            self.t[0].right(90)
         
        self.t[0].right(90)
        self.t[0].forward(35*l)
        for c in range(2):
            self.t[0].forward(30*l)
            self.t[0].left(90)
            self.t[0].forward(25*l)
            self.t[0].right(90)
            self.t[0].forward(10*l)
            for c in range(2):
                self.t[0].right(90)
                self.t[0].forward(5*l)
                self.t[0].backward(5*l)
                self.t[0].left(90)
                self.t[0].forward(10*l)
            self.t[0].right(90)
            self.t[0].forward(25*l)
            self.t[0].left(90)
        self.t[0].right(90)
        self.t[0].forward(30*l)
     
        self.t[0].backward(30*l)
        self.t[0].right(90)
        self.t[0].penup()
        self.t[0].forward(90*l)
        self.t[0].pendown()
        for c in range(4):
            for c in range(2):
                self.t[0].left(90)
                self.t[0].forward(50*l)
                self.t[0].backward(50*l)
                self.t[0].right(90)
                self.t[0].penup()
                self.t[0].forward(7*l)
                self.t[0].pendown()
            self.t[0].penup()
            self.t[0].forward(7*l)
            self.t[0].pendown()
        self.t[0].penup()
        self.t[0].forward(12*l)
        self.t[0].pendown()
        for c in range(2):
            for c in range(2):
                self.t[0].left(90)
                self.t[0].forward(50*l)
                self.t[0].backward(50*l)
                self.t[0].right(90)
                self.t[0].penup()
                self.t[0].forward(6*l)
                self.t[0].pendown()
            self.t[0].penup()
            self.t[0].forward(4*l)
            self.t[0].pendown()
     
        self.t[0].seth(h)
        self.t[0].penup()
        self.t[0].goto(x,y)
        self.t[0].forward(120*l)
        self.t[0].left(90)
        self.t[0].forward(20*l)
        self.t[0].right(90)
        self.t[0].pendown()
        for i in range(2):
            for c in range(4):
                self.t[0].forward((30-(i*10))*l)
                self.t[0].left(90)
            self.t[0].left(45)
            self.t[0].penup()
            self.t[0].forward((14-(i*7))*l)
            self.t[0].pendown()
            self.t[0].right(45)
            for c in range(4):
                self.t[0].forward(10*l)
                self.t[0].left(90)
            self.t[0].left(90)
            self.t[0].penup()
            self.t[0].forward(20*l)
            self.t[0].right(90)
            self.t[0].backward(5*l)
            self.t[0].pendown()
        self.x=self.t[0].xcor()
        self.y=self.t[0].ycor()-5
        self.t[0].penup()
        self.t[0].goto(x,y)
        self.t[0].pendown()
        self.sc.update()

    def bag(self,xt,yt,x=None,y=None,h=0,l=0.5):
        self.t[1].clear()
        if xt==None and yt==None:
            xt=self.xt
            yt=self.yt
        else:
            if yt<-300 or yt>300 or xt<-350 or xt>350:
                xt=self.xt
                yt=self.yt
            else:
                self.xt=xt
                self.yt=yt
        if x==None and y==None:
            x=self.x
            y=self.y
        else:
            self.x=x
            self.y=y
        self.t[1].seth(h)
        self.t[1].penup()
        self.t[1].goto(x,y)
        self.t[1].forward(135*l)
        self.t[1].left(90)
        self.t[1].forward(70*l)
        self.t[1].right(90)
        self.t[1].pendown()
        self.t[1].seth(self.t[1].towards(xt,yt))
        self.t[1].forward(50*l)
        self.sc.update()

    def catbag(self,x,y,h,l):
        self.cat(x,y,h,l)
        #self.bag(None,None,x,y,h,l)
        self.sc.update()

    def left(self):

        left=self.t[0].xcor()-10
        if -350<left<200:
            pass
        elif -300>left:
            left=-350

        self.catbag(left,-270,0,0.5)

    def right(self):

        right=self.t[0].xcor()+10
        if -350<right<200:
            pass
        elif 150<right:
            right=200

        self.catbag(right,-270,0,0.5)

    def shoot(self,xt,yt,turtle):
        turtle.st()
        turtle.goto(self.x,self.y)
        turtle.setheading(turtle.towards(xt,yt))
        self.shooting=True
        self.sc.update()

    def onmove(self,fun):
        if fun is None:
            self.sc.cv.unbind('<Motion>')
        else:
            def eventfun(event):
                fun(self.sc.cv.canvasx(event.x),-self.sc.cv.canvasy(event.y))
            self.sc.cv.bind('<Motion>', eventfun)
        self.sc.update()

    def OnSuperShoot(self,fun):
        if fun is None:
            self.sc.cv.unbind('<B1-Motion>')
        else:
            def eventfun(event):
                if self.countSB<50:
                    x=self.sc.cv.canvasx(event.x)
                    y=-self.sc.cv.canvasy(event.y)
                    if y<-300 or y>300 or x<-350 or x>350:
                        self.Pout(event)
                    else:
                        _=Turtle()
                        _.shapesize(1,2)
                        _.color("light blue")
                        _.penup()
                        self.Superbullet.append(_)
                        self.countSB+=1
                        fun(x,y,self.Superbullet[self.countSB-1])
                else:
                    self.Pout(event)
            self.sc.cv.bind('<B1-Motion>', eventfun)
        self.sc.update()

    def Pout(self,event=None):
        self.TFC=False
        self.PC=0
        self.t[7].clear()

    def onc(self,event):
        x=self.sc.cv.canvasx(event.x)
        y=-self.sc.cv.canvasy(event.y)
        if y<-300 or y>300 or x<-350 or x>350:
            self.shooting=False
        else:
            self.shooting=True
            self.TFC=True

    def onshoot(self,fun):
        if fun is None:
            self.sc.cv.unbind('<ButtonRelease-1>')
        else:
            def eventfun(event):
                self.Pout(event)
                x=self.sc.cv.canvasx(event.x)
                y=-self.sc.cv.canvasy(event.y)
                if y<-300 or y>300 or x<-350 or x>350:
                    pass
                else:
                    _=Turtle()
                    _.shapesize(1,2)
                    _.color("green")
                    _.penup()
                    self.bullet.append(_)
                    self.countB+=1
                    fun(x,y,self.bullet[self.countB-1])
            self.sc.cv.bind('<ButtonRelease-1>', eventfun)
        self.sc.update()

    def play(self):
        global kill
        while 1:
            self.sc.onkeypress(self.left,"a")
            self.sc.onkeypress(self.right,"d")
            self.sc.cv.bind('<Button-1>',self.onc)
            #self.onmove(self.bag)
            if self.TFC:
                if self.PC<200:
                    self.PC+=1
                    self.t[7].penup()
                    self.t[7].goto(370,-300+self.PC)
                    self.t[7].pendown()
                    self.t[7].color("blue")
                    self.t[7].forward(20)
                else:
                    pass

            if self.PC>=200 and self.shooting:
                self.onshoot(None)
                self.OnSuperShoot(self.shoot)
                self.sc.cv.bind('<ButtonRelease-1>',self.Pout)
            elif self.PC<200 and self.shooting:
                if self.countB>=3:
                    self.onshoot(None)
                    self.sc.cv.bind('<ButtonRelease-1>',self.Pout)
                else:
                    self.OnSuperShoot(None)
                    self.onshoot(self.shoot)
                    
            if self.monsterbullet!=[] and self.bullet!=[]:
                for c in self.monsterbullet:
                    cx=c.xcor()
                    cy=c.ycor()
                    for i in self.bullet:
                        ix=i.xcor()
                        iy=i.ycor()
                        if -10<=(cx-ix)<=10 and -10<=(cy-iy)<=10:
                            c.ht()
                            self.monsterbullet.remove(c)
                            self.countMSB-=1
                            i.ht()
                            self.bullet.remove(i)
                            self.countB-=1
            
            if self.bullet!=[]:
                for c in self.bullet:
                    x=c.xcor()
                    y=c.ycor()
                    if -15<=(x-(self.t[6].xcor()+15))<=15 and -15<=(y-(self.t[6].ycor()+15))<=15:
                        self.Exspeed=0
                        self.LRR=r(-335,335)
                        self.LRC=ch([-1,1])
                        self.Exspeed+=r(0,5)*self.LRC
                        c.ht()
                        self.bullet.remove(c)
                        self.countB-=1
                        self.score+=1
                        self.Elive-=1
                        self.t[3].clear()
                        self.t[3].write("Enemy Live:%s"%self.Elive,0,"left",("Arial", 30, "normal"))
                        if self.t[6].ycor()<-232.5:
                            self.Eyspeed=0

                    elif (y<-300 or y>300 or x<-350 or x>350):
                        #self.shooting=False
                        c.ht()
                        self.bullet.remove(c)
                        self.countB-=1
                    elif (y>=-300 or y<=300) and (x>=-350 or x<=350):
                        c.forward(10)

            if self.Superbullet!=[]:
                for c in self.Superbullet:
                    x=c.xcor()
                    y=c.ycor()
                    if -15<=(x-(self.t[6].xcor()+15))<=15 and -15<=(y-(self.t[6].ycor()+15))<=15:
                        self.Exspeed=0
                        self.LRR=r(-335,335)
                        self.LRC=ch([-1,1])
                        self.Exspeed+=r(0,5)*self.LRC
                        c.ht()
                        self.Superbullet.remove(c)
                        self.countSB-=1
                        self.score+=1
                        self.Elive-=1
                        self.t[3].clear()
                        self.t[3].write("Enemy Live:%s"%self.Elive,0,"left",("Arial", 30, "normal"))
                        if self.t[6].ycor()<-232.5:
                            self.Eyspeed=0

                    elif (y<-300 or y>300 or x<-350 or x>350):
                        #self.shooting=False
                        c.ht()
                        self.Superbullet.remove(c)
                        self.countSB-=1
                    elif (y>-300 or y<300) and (x>-350 or x<350):
                        c.forward(10)

            if self.monsterbullet!=[]:
                for c in self.monsterbullet:
                    x=c.xcor()
                    y=c.ycor()
                    if (-37.5<=(x-(self.t[0].xcor()+37.5))<=37.5 and -32.5<=(y-(self.t[0].ycor()))<=35) or (-37.5<=(x-(self.t[0].xcor()+107.5))<=37.5 and -32.5<=(y-(self.t[0].ycor()))<=10):
                        c.ht()
                        self.monsterbullet.remove(c)
                        self.countMSB-=1
                        self.live-=1
                        self.t[5].clear()
                        self.t[5].write("Live:%s"%self.live,0,"left",("Arial", 30, "normal"))
                    
                    elif (y<-300 or y>300 or x<-350 or x>350):
                        c.ht()
                        self.monsterbullet.remove(c)
                        self.countMSB-=1
                    elif (y>-300 or y<300) and (x>-350 or x<350):
                        c.forward(10)

            if (-37.5<=(self.t[6].xcor()+15-(self.t[0].xcor()+37.5))<=37.5 and -32.5<=(self.t[6].ycor()+15-(self.t[0].ycor()))<=35) or (-37.5<=(self.t[6].xcor()+15-(self.t[0].xcor()+107.5))<=37.5 and -32.5<=(self.t[6].ycor()+15-(self.t[0].ycor()))<=10):
                self.live-=2
                self.t[5].clear()
                self.t[5].write("Live:%s"%self.live,0,"left",("Arial", 30, "normal"))
                self.Eyspeed=0
                
            if self.Elive>0 and self.live>0:
                self.monstermove(self.LV1,self.t[6])
                self.monstershoot()
            elif self.Elive<=0 and self.live>0:
                kill+=1
                self.t[4].clear()
                self.t[4].write("Kill:%s"%kill,0,"left",("Arial", 30, "normal"))
                self.onshoot(None)
                self.OnSuperShoot(None)
                self.onmove(None)
                self.sc.onkeypress(None,"a")
                self.sc.onkeypress(None,"d")
                break
            elif self.Elive>0 and self.live<=0:
                self.t[4].clear()
                self.t[4].write("you die Game Over",0,"left",("Arial", 30, "normal"))
                kill=0
                self.onshoot(None)
                self.OnSuperShoot(None)
                self.onmove(None)
                self.sc.onkeypress(None,"a")
                self.sc.onkeypress(None,"d")
                break
            elif self.Elive<=0 and self.live<=0:
                self.t[4].clear()
                self.t[4].write("you die Game Over",0,"left",("Arial", 30, "normal"))
                kill=0
                self.onshoot(None)
                self.OnSuperShoot(None)
                self.onmove(None)
                self.sc.onkeypress(None,"a")
                self.sc.onkeypress(None,"d")
                break
            self.sc.update()
        self.sc.update()
    
    def clear(self):
        for c in self.t:
            c.clear()
            c.ht()
        self.t.clear()
        for c in self.bullet:
            c.clear()
            c.ht()
        self.bullet.clear()
        for c in self.Superbullet:
            c.clear()
            c.ht()
        self.Superbullet.clear()
        self.__init__()
        self.sc.update()

kill=0
lol=game()
def reset():
    lol.clear()
    lol.play()
sc.listen()
sc.onkey(reset,"r")
sc.update()





