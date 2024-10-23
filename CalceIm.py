from tkinter import *

def onclick(event):
    text = event.widget.cget('text')
    current = v.get()
    
    if text == "=":
        try:
            total = eval(current)
            v.set(total)
        except Exception:
            v.set("Error")
    elif text == "C":
        v.set("")
    else:
        # Prevent multiple operators or dots in sequence
        if text in "+-*/.%":
            if current and current[-1] in "+-*/.%":
                return  # Ignore if last char is an operator or dot
        v.set(current + text)

a = Tk()
a.geometry("250x350")
a.title("Calculator")

v = StringVar()

# Entry field with text aligned to the right
en = Entry(a, textvariable=v, font="Arial 14", justify='right')
en.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
    ('%', 5, 0), ('=', 5, 1, 3)
]

# Create and place buttons using grid
for (text, row, col, colspan) in buttons:
    b = Button(a, text=text, font="Arial 14", width=5, height=2)
    if colspan:
        b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
    else:
        b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", onclick)

a.mainloop()
