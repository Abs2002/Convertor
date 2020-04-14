from tkinter import *
from tkinter.ttk import *

rt=Tk()
rt.geometry("400x150")
rt.title("Area Converter")

l1=Label(rt, text="(1)")
l2=Label(rt, text="(2)")

l1.place(x=10, y=30)
l2.place(x=10, y=60)

def tg():

    if cm.get()==cm['values'][0]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(int(sc1.get())*10000)
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str(int(sc2.get())/10000)
            sc1.set(a)

    elif cm.get()==cm['values'][1]:
        if sc1.get() != "" and sc2.get() == "":
            a=str(int(sc1.get())*4046)
            sc2.set(a)
        elif sc1.get() == "" and sc2.get() != "":
            a = str(int(sc2.get())/4046)
            sc1.set(a)

    elif cm.get() == cm['values'][2]:
        if sc1.get() != "" and sc2.get() == "":
            a=str(float(sc1.get())*10.76)
            sc2.set(a)
        elif sc1.get() == "" and sc2.get() != "":
            a = str(float(sc2.get())/10.76)
            sc1.set(a)


sc1=StringVar()
sc2=StringVar()

en1=Entry(rt, textvariable=sc1)
en2=Entry(rt, textvariable=sc2)

en1.place(x=30, y=30)
en2.place(x=30, y=60)

cm=Combobox(rt, width=22)
cm['values']=("(1)Sq meter <-> (2)Sq centimeter", "(1)Acre <-> (2)Sq meter", "(1)Sq meter <-> (2)Sq foot", "select any one")
cm.current(3)
cm.place(x=200, y=30)

b1=Button(rt, text="click here", command=tg)

def rg():
    sc1.set("")
    sc2.set("")
b2=Button(rt, text="clear", command=rg)

b1.place(x=200, y=60)
b2.place(x=280, y=60)

rt.mainloop()

