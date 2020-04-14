from tkinter import *
from tkinter.ttk import *

rt=Tk()
rt.geometry("400x150")
rt.title("Temperature Converter")

l1=Label(rt, text="(1)")
l2=Label(rt, text="(2)")

l1.place(x=10, y=30)
l2.place(x=10, y=60)

def tg():

    if cm.get()==cm['values'][0]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(9/5*(int(sc1.get())+32))
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str((int(sc2.get())-32)*5/9)
            sc1.set(a)

    elif cm.get()==cm['values'][1]:
        if sc1.get() != "" and sc2.get() == "":
            a=str(int(sc1.get())+273)
            sc2.set(a)
        elif sc1.get() == "" and sc2.get() != "":
            a = str(int(sc2.get())-273)
            sc1.set(a)

    elif cm.get() == cm['values'][2]:
        if sc1.get() != "" and sc2.get() == "":
            a=str(((int(sc1.get())-32)*5/9)+273)
            sc2.set(a)
        elif sc1.get() == "" and sc2.get() != "":
            a = str(((int(sc2.get())-273)*9/5)+32)
            sc1.set(a)


sc1=StringVar()
sc2=StringVar()

en1=Entry(rt, textvariable=sc1)
en2=Entry(rt, textvariable=sc2)

en1.place(x=30, y=30)
en2.place(x=30, y=60)

cm=Combobox(rt, width=22)
cm['values']=("(1)Celcius <-> (2)Farheinheit", "(1)Celcius <-> (2)Kelvin", "(1)Farhenheit <-> (2)Kelvin", "select any one")
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

