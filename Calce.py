import tkinter as tk
root=tk.Tk()
root.title("Calculator")
buttons=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    'C','0','=','+'
]
def onclick(event):
    text=event.widget.cget('text')
    if text=="=":
        total=eval(en.get())
        en.delete(0,tk.END)
        en.insert(tk.END,str(total))
    elif text=="C":
        en.delete(0,tk.END)
    else:
        en.insert(tk.END,text)
en=tk.Entry(root,width=16)
en.grid(row=0,column=0,columnspan=4)
row_value=1
col_value=0
for button in buttons:
    btn=tk.Button(root,text=button,width=4,height=2)
    btn.grid(row=row_value, column=col_value)
    btn.bind("<Button-1>",onclick)
    col_value+=1
    if col_value>3:
        col_value=0
        row_value+=1
root.mainloop()