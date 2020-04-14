from tkinter import *
import os
rt=Tk()

rt.geometry("538x260")
rt.maxsize("540", "260")
rt.title("Convertor")
rt.configure(background="black")

def op1():
    os.system("areaconv.py")
def op2():
    os.system("gstconv.py")
def op3():
    os.system("lengthconv.py")
def op4():
    os.system("numconv.py")
def op5():
    os.system("speedconv.py")
def op6():
    os.system("tempconv.py")
def op7():
    os.system("timeconv.py")
def op8():
    os.system("volumeconv.py")
def op9():
    os.system("weightconv.py")



b1=Button(rt, text="Area Convertor", font=(22), padx=25,pady=25,  command=op1)
b2=Button(rt, text="GST Convertor",  font=(22), padx=25,pady=25, command=op2)
b3=Button(rt, text="Length Convertor",  font=(22), padx=25,pady=25,  command=op3)
b4=Button(rt, text="Number Convertor",   font=(22), padx=15,pady=25, command=op4)
b5=Button(rt, text="Speed Convertor",   font=(22), padx=18,pady=25, command=op5)
b6=Button(rt, text="Temp Convertor",   font=(22), padx=28,pady=25, command=op6)
b7=Button(rt, text="Time Convertor",   font=(22), padx=25,pady=25, command=op7)
b8=Button(rt, text="Volume Convertor",   font=(22), padx=15,pady=25, command=op8)
b9=Button(rt, text="Weight Convertor",   font=(22), padx=24,pady=25, command=op9)

b1.place(x=5, y=5)
b2.place(x=178, y=5)
b3.place(x=349, y=5)
b4.place(x=5, y=90)
b5.place(x=178, y=90)
b6.place(x=349, y=90)
b7.place(x=5, y=175)
b8.place(x=178, y=175)
b9.place(x=349, y=175)

rt.mainloop()