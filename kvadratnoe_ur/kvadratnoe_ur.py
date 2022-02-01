from tkinter import *
from math import *
import matplot.pyplot as plt #Y=...
import numpy as np #x =[min,max] 
global D,t
D=-1
t="net resheniy"
graf=False

a=0
b=0
c=0
D=0
x1=0
x2=0
def vvod(event):
    t=a.get()
    lbl.configure(text=t)
    a.delete(0,END)

def kvadr():
    global D,t,graf
    a=int(txt.get())
    b=int(txt2.get())
    c=int(txt3.get())
    D=(b)**2-4*(a)*(c)
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        if (float(txt.get())==0 and float(txt2.get())==0 and float(txt3.get())==0):
            otvet.configure(text=f"Ne mozet bit 0")
            txt.configure(bg="red")
            txt2.configure(bg="red")
            txt3.configure(bg="red")
        elif float(txt.get())==0 and float(txt2.get())!=0 and float(txt3.get())!=0:
            otvet.configure(text=f"Ne mozet bit 0")
            txt.configure(bg="red")
            graf=False
        else:
            a_=float(a.get())
            b_=float(b.get())
            c_=float(c.get())
            D=b_*b_-4*a_*c_
            if D>0:
                x1_=round((-1*b_+sqrt(D))/(2*a_),2)
                x2_=round((-1*b_-sqrt(D))/(2*a_),2)
                t=f"X1={x1_}, \nX2={x2_}"
                graf=True
            elif D==0:
                x1_=round((-1*b_)/(2*a_),2)
                t=f"X1={x1_}"
                graf=True
            else:
                t="Korney net"
                graf=False
            otvet.configure(text=f"D={D}\n{t}")
            txt.configure(bg="lightblue")
            txt2.configure(bg="lightblue")
            txt3.configure(bg="lightblue")   
    else:
        if txt.get()=="":
            txt.configure(bg="red")
        if txt2.get()=="":
            txt2.configure(bg="red")
        if txt3.get()=="":
            txt3.configure(bg="red")
        else:
            txt.configure(bg="lightblue")
            txt2.configure(bg="lightblue")
            txt3.configure(bg="lightblue")
        graf=False
    return graf,D,t
def graafik():
    if D >= 0:
        x1=-b+sqrt(D)/2*a
        x2=-b-sqrt(D)/2*a
        otvet.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
    elif D==0:
        x1=-b/2*a
        x2=-b/2*a
        otvet.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
    else:
        otvet.configure(text=f"Diskriminant menshe 0, x1 i x2 ne vy4islyt \nD={D}")
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="Umenshit okno")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="Uveli4it okno")
        t=0

def figura():
    valik=var.get()
    otvet.configure(text=valik)
    if valik==1:
        kala()
    elif valik==2:
        vihmavari()
    elif valik==3:
        prillid()
    else:
        konn()
def kala(): 
    x1 = np.arange(0, 9.5, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)#min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)#min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)#min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)#min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)#min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)#min max step
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Kit')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def prillid():
    x1=np.arange(-9,-0.5,0.5)
    y1=-1/16*(x1+5)**2+2
    x2=np.arange(1,9.5,0.5)
    y2=-1/16*(x2-5)**2+2
    x3=np.arange(-9,-0.5,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9.5,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-5.5,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9.5,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1.5,0.5)
    y7=-0.5*x7**2+1.5
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('O4ki')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def konn():
    x1 = np.arange(0, 9.5, 0.5)
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)
    y2=0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Lyaguha')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def vihmavari():
    x1 = np.arange(-12, 12.5, 0.5)
    y1 = (-1/18)*x1*x1+12
    x2 = np.arange(-4, 4.5, 0.5)
    y2 = (-1/8)*x2*x2+6
    x3 = np.arange(-12, -3.5, 0.5)
    y3 = (-1/8)*(x3+8)**2+6
    x4 = np.arange(4, 12.5, 0.5)
    y4 = (-1/8)*(x4-8)**2+6
    x5 = np.arange(-4, 0.2, 0.5)
    y5 = 2*(x5+3)**2-9
    x6 = np.arange(-4, 0.7, 0.5)
    y6 = 1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1, y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Zont')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()


def graafik():
    graf,D,t=kvadr()
    if graf==True:
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x1=np.arange(x0-10, x0+10, 0.5)#min max step [min,max]
        y1=a_*x1*x1+b_*x1+c_
        fig=plt.figure()
        plt.plot(x0, y0, x1, y1, "r-d")
        plt.title("Kvadratnoe uravnenie")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"Vershina paraboli ({x0},{y0})"
    else:
        text=f"Grafik net vozmoznosti postroit"
        otvet.configure(text=f"D={D}\n{t}\n{text}")
t=0

aken=Tk()
aken.title("Kvadratnoe uravnenie")
aken.geometry("650x240")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)


lbl=Label(aken,text="Reshenie kvadratnogo uravneniya",height=3,width=30,font="Arial 20",fg="green",bg="lightblue",relief=FLAT)#.pack()
lbl.pack()

txt=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt.pack(side=LEFT)

lb2=Label(aken,text="  x**2+  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb2.pack(side=LEFT)

txt2=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt2.pack(side=LEFT)

lb3=Label(aken,text="  x+  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb3.pack(side=LEFT)

txt3=Entry(aken,width=4,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt3.pack(side=LEFT)

lb4=Label(aken,text="  =0  ",height=3,width=6,font="Arial 20",fg="green",relief=FLAT)#.pack()
lb4.pack(side=LEFT)

nupp=Button(aken,text="Reshit!",font="Arial 20",width=15,bg="green",fg="black",relief=RAISED,command=kvadr)
nupp.pack(side=LEFT)

otvet=Label(aken,text="Reshenie",height=3,width=40,font="Arial 20",fg="black",bg="yellow",relief="solid")#.pack()
otvet.pack(side=BOTTOM)

btn_veel=Button(f2,text="Uveli4it okno",font="Calibri 26",bg="green",command=veel)
btn_veel.pack(side=TOP)
var=IntVar()
var.set
r1=Radiobutton(f2,text="Kit",variable=var,value=1,font="Calibri 26",command=figura)#command=kala
r2=Radiobutton(f2,text="Konn",variable=var,value=2,font="Calibri 26",command=figura)#command=kala
r3=Radiobutton(f2,text="Lyaguha",variable=var,value=3,font="Calibri 26",command=figura)#command=kala
r4=Radiobutton(f2,text="Vihmavari",variable=var,value=4,font="Calibri 26",command=figura)#command=kala


r1.pack()
r2.pack()
r3.pack()

aken.mainloop()




#def kvadr():
#    a=int(txt.get())
#    b=int(txt2.get())
#    c=int(txt3.get())
#    D=(b)**2-4*(a)*(c)
#    if D >= 0:
#        x1=-b+sqrt(D)/2*a
#        x2=-b-sqrt(D)/2*a
#        lb5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
#    elif D==0:
#        x1=-b/2*a
#        x2=-b/2*a
#        lb5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
#    else:
#        lb5.configure(text=f"Diskriminant menshe 0, x1 i x2 ne vy4islyt \nD={D}")
