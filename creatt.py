from tkinter import*
import tkinter as ttk
a=Tk()
a.geometry("200x300")
a.maxsize(200,300)
a.minsize(200,300)

def onclick(event):
    text=event.widget.cget('text')
    # print("text",text)
    if text=="=":
        data=en.get()
        total=eval(data)
        v.set(total)
        en.update()
    elif text=="C":
        en.delete(0,15)
    else:
        data=en.get()
        v.set(data+text)
        en.update()
    
head=Label(text="Calculator")
head.place(x=10,y=5)

v=StringVar()
en=Entry(textvariable=v)
en.config(width=29)
en.place(x=12,y=25)

b1=Button(text="7")
b1.config(width=4,height=2)
b1.bind("<Button-1>",onclick)
b1.place(x=12,y=55)

b2=Button(text="8")
b2.config(width=4,height=2)
b2.place(x=55,y=55)
b2.bind("<Button-1>",onclick)

b3=Button(text="9")
b3.config(width=4,height=2)
b3.place(x=98,y=55)
b3.bind("<Button-1>",onclick)

b4=Button(text="4")
b4.config(width=4,height=2)
b4.place(x=12,y=100)
b4.bind("<Button-1>",onclick)

b5=Button(text="5")
b5.config(width=4,height=2)
b5.place(x=55,y=100)
b5.bind("<Button-1>",onclick)

b6=Button(text="6")
b6.config(width=4,height=2)
b6.place(x=98,y=100)
b6.bind("<Button-1>",onclick)

b7=Button(text="1")
b7.config(width=4,height=2)
b7.place(x=12,y=145)
b7.bind("<Button-1>",onclick)

b8=Button(text="2")
b8.config(width=4,height=2)
b8.place(x=55,y=145)
b8.bind("<Button-1>",onclick)

b9=Button(text="3")
b9.config(width=4,height=2)
b9.place(x=98,y=145)
b9.bind("<Button-1>",onclick)

b10=Button(text="C")
b10.config(width=4,height=2)
b10.place(x=12,y=190)
b10.bind("<Button-1>",onclick)

b11=Button(text="0")
b11.config(width=4,height=2)
b11.place(x=55,y=190)
b11.bind("<Button-1>",onclick)

b12=Button(text=".")
b12.config(width=4,height=2)
b12.place(x=98,y=190)
b12.bind("<Button-1>",onclick)

b13=Button(text="/")
b13.config(width=6,height=2)
b13.place(x=140,y=190)
b13.bind("<Button-1>",onclick)

b14=Button(text="+")
b14.config(width=6,height=2)
b14.place(x=140,y=55)
b14.bind("<Button-1>",onclick)

b15=Button(text="-")
b15.config(width=6,height=2)
b15.place(x=140,y=100)
b15.bind("<Button-1>",onclick)

b16=Button(text="*")
b16.config(width=6,height=2)
b16.place(x=140,y=145)
b16.bind("<Button-1>",onclick)

b17=Button(text="%")
b17.config(width=6,height=2)
b17.place(x=140,y=235)
b17.bind("<Button-1>",onclick)

b18=Button(text="=")
b18.config(width=16,height=2)
b18.place(x=12,y=235)
b18.bind("<Button-1>",onclick)

a.mainloop()