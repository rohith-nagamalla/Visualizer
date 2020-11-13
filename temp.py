from digitalTdigital import plot
from digitalTanalog import plot2
from tkinter import *

root = Tk()

myLabel=Label(root,text="Vizualizer")
myLabel.pack()

myLabel=Label(root,text="1)Unipolar-NRZ 2)NRZ-L 3)NRZ-I 4)Polar-RZ 5)Manchester 6)Dif_Man 7)A-M-I 8)ASK 9)FSK 10)PSK")
myLabel.pack()

e=Entry(root,width=50)
e.pack()
e.insert(0,"Enter no. of data")


li1=""

def myClick():
    myLabel=Label(root,text=e.get())
    myLabel.pack()
    def myClick2():
        myLabel=Label(root,text=e2.get())
        myLabel.pack()
    e2=Entry(root,width=50)
    e2.pack()
    e2.insert(0,"Enter digital data")
    myButton2=Button(root, text="enter",command=myClick2)
    myButton2.pack()

myButton=Button(root, text="enter",command=myClick)
myButton.pack()


root.mainloop()

