from tkinter import *
from math import *

a=0
b=0
c=0
D=0
x1=0
x2=0
def vvod(event):
    t=txt.get()
    lbl.configure(text=t)
    txt.delete(0,END)

def kvadr(event):
    a=int(txt.get())
    b=int(txt2.get())
    c=int(txt3.get())
    D=(b)**2-4*(a)*(c)
    if D >= 0:
        x1=-b+sqrt(D)/2*a
        x2=-b-sqrt(D)/2*a
        lb5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
    elif D==0:
        x1=-b/2*a
        x2=-b/2*a
        lb5.configure(text=f"D={D}\n x1={x1}\n x2={x2}")
    else:
        lb5.configure(text=f"Diskriminant menshe 0, x1 i x2 ne vy4islyt \nD={D}")


aken=Tk()
aken.title("Kvadratnoe uravnenie")
aken.geometry("800x500")


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

nupp=Button(aken,text="Reshit!",font="Arial 20",width=15,bg="green",fg="black",relief=RAISED)
nupp.pack(side=LEFT)
nupp.bind("<Button-1>",kvadr)

lb5=Label(aken,text="Reshenie",height=3,width=40,font="Arial 20",fg="black",bg="yellow",relief="solid")#.pack()
lb5.place(x=80,y=360)

aken.mainloop()
