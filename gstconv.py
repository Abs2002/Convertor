from tkinter import *
from tkinter.ttk import *
rt=Tk()
rt.geometry("400x150")
rt.title("GST Calculator")

l1=Label(rt, text="Original Price")
l1.place(x=10, y=30)

l2=Label(rt, text="GST Slab")
l2.place(x=10, y=60)

def qt():
    if cm.get()==cm['values'][0]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(int(sc1.get())+(5/100*int(sc1.get())))
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str((100*int(sc2.get()))/(100+5))
            sc1.set(a)

    elif cm.get()==cm['values'][1]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(int(sc1.get())+(12/100*int(sc1.get())))
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str((100*int(sc2.get()))/(100+12))
            sc1.set(a)

    elif cm.get()==cm['values'][2]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(int(sc1.get())+(18/100*int(sc1.get())))
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str((100*int(sc2.get()))/(100+18))
            sc1.set(a)

    elif cm.get()==cm['values'][3]:
        if sc1.get()!="" and sc2.get()=="":
            a=str(int(sc1.get())+(28/100*int(sc1.get())))
            sc2.set(a)
        elif sc1.get()=="" and sc2.get()!="":
            a=str((100*int(sc2.get()))/(100+28))
            sc1.set(a)

cm=Combobox(rt, width=22)
cm['values']=("5%", "12%", "18%", "28%", "select any one")
cm.current(4)
cm.place(x=100, y=60)

sc1=StringVar()
sc2=StringVar()

en1=Entry(rt, textvariable=sc1, width=25)
en1.place(x=100, y=30)

l2=Label(rt, text="Final price")
l2.place(x=10, y=90)

en2=Entry(rt, textvariable=sc2, width=25)
en2.place(x=100, y=90)

b1=Button(rt, text="click here", command=qt)

def rg():
    sc1.set("")
    sc2.set("")
b2=Button(rt, text="clear", command=rg)

b1.place(x=280, y=60)
b2.place(x=280, y=90)



rt.mainloop()