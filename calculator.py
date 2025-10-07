from tkinter import *
import re

root = Tk()
root.title("Calculator App")
root.geometry("490x570")
root.resizable(False, False)

equation = StringVar()

def calculator(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            expression = equation.get().replace("x", "*")
            expression = re.sub(r'(\d+(?:\.\d+)?)%(\d+(?:\.\d+)?)', r'(\1/100)*\2', expression)
            expression = re.sub(r'(\d+(?:\.\d+)?)%', r'(\1/100)', expression)


            result = str(eval(expression))
            equation.set(result)
        except:
            equation.set("Error")

    elif text == "C":
        equation.set("")
    elif text == "del":
        current = equation.get()
        equation.set(current[:-1])
    else:
        if equation.get() == "Error":
            equation.set("")
        equation.set(equation.get() + text)

entry = Entry(root, font=("Arial", 31), relief=SUNKEN, borderwidth=10, textvariable=equation)
entry.grid(row=0, column=0, rowspan=1, columnspan=4, pady=10)
entry.config(state="readonly")


button = Button(root, text="C", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=1, column=0)
button.bind("<Button-1>", calculator)

button = Button(root, text="%", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=1, column=1)
button.bind("<Button-1>", calculator)

button = Button(root, text="del", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=1, column=2)
button.bind("<Button-1>", calculator)

button = Button(root, text="/", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=1, column=3)
button.bind("<Button-1>", calculator)

button = Button(root, text="7", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=0)
button.bind("<Button-1>", calculator)

button = Button(root, text="8", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=1)
button.bind("<Button-1>", calculator)

button = Button(root, text="9", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=2)
button.bind("<Button-1>", calculator)

button = Button(root, text="x", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=2, column=3)
button.bind("<Button-1>", calculator)

button = Button(root, text="4", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=0)
button.bind("<Button-1>", calculator)

button = Button(root, text="5", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=1)
button.bind("<Button-1>", calculator)

button = Button(root, text="6", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=2)
button.bind("<Button-1>", calculator)

button = Button(root, text="-", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=3, column=3)
button.bind("<Button-1>", calculator)

button = Button(root, text="1", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=0)
button.bind("<Button-1>", calculator)

button = Button(root, text="2", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=1)
button.bind("<Button-1>", calculator)

button = Button(root, text="3", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=2)  
button.bind("<Button-1>", calculator)  

button = Button(root, text="+", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6, bg="orange")
button.grid(row=4, column=3)
button.bind("<Button-1>", calculator)

button = Button(root, text="00", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=0)
button.bind("<Button-1>", calculator)

button = Button(root, text="0", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=1)
button.bind("<Button-1>", calculator)

button = Button(root, text=".", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=2)
button.bind("<Button-1>", calculator)

button = Button(root, text="=", bg="orange", font=("Arial", 32), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=3)
button.bind("<Button-1>", calculator)

root.mainloop()
