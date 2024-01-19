from tkinter import *

top = Tk()
top.title("Calculator")
top.geometry("320x500")

# set columns and rows
top.columnconfigure([0,1,2,3], minsize=80, weight=1)
top.rowconfigure([0,1,2,3,4], minsize=100, weight=1)

# set entry box / display
equation = StringVar()
fill = ""
display = Entry(top, font=(30), justify=RIGHT, textvariable = equation)
display.grid(row=0, column=1, columnspan=3, ipady=15)

# update entry box, when buttons are clicked
def press(num: int):
    global fill
    fill += str(num)
    equation.set(fill)

# count and update result to the entry box
def equal():
    global fill
    result = str(eval(fill))
    equation.set(result)

# clear entry box
def clear():
    global fill
    fill = ""
    equation.set("")

# buttons
zero = Button(text="0", fg="black", font=(30), command=lambda: press(0))
zero.grid(row=4, column=0, ipady=15, ipadx=15)
one = Button(text="1", fg="black", font=(30), command=lambda: press(1))
one.grid(row=3, column=0, ipady=15, ipadx=15)
two = Button(text="2", fg="black", font=(30), command=lambda: press(2))
two.grid(row=3, column=1, ipady=15, ipadx=15)
three = Button(text="3", fg="black", font=(30), command=lambda: press(3))
three.grid(row=3, column=2, ipady=15, ipadx=15)
four = Button(text="4", fg="black", font=(30), command=lambda: press(4))
four.grid(row=2, column=0, ipady=15, ipadx=15)
five = Button(text="5", fg="black", font=(30), command=lambda: press(5))
five.grid(row=2, column=1, ipady=15, ipadx=15)
six = Button(text="6", fg="black", font=(30), command=lambda: press(6))
six.grid(row=2, column=2, ipady=15, ipadx=15)
seven = Button(text="7", fg="black", font=(30), command=lambda: press(7))
seven.grid(row=1, column=0, ipady=15, ipadx=15)
eight = Button(text="8", fg="black", font=(30), command=lambda: press(8))
eight.grid(row=1, column=1, ipady=15, ipadx=15)
nine = Button(text="9", fg="black", font=(30), command=lambda: press(9))
nine.grid(row=1, column=2, ipady=15, ipadx=15)
addition = Button(text="+", fg="black", font=(30), command=lambda: press("+"))
addition.grid(row=4, column=3, ipady=15, ipadx=15)
subtraction = Button(text="-", fg="black", font=(30), command=lambda: press("-"))
subtraction.grid(row=3, column=3, ipady=15, ipadx=15)
multiplication = Button(text="*", fg="black", font=(30), command=lambda: press("*"))
multiplication.grid(row=2, column=3, ipady=15, ipadx=15)
division = Button(text="/", fg="black", font=(30), command=lambda: press("/"))
division.grid(row=1, column=3, ipady=15, ipadx=15)
decimal = Button(text=".", fg="black", font=(30), command=lambda: press("."))
decimal.grid(row=4, column=1, ipady=15, ipadx=15)
equal = Button(text="=", fg="black", font=(30), command=equal)
equal.grid(row=4, column=2, ipady=15, ipadx=15)
clear = Button(text="C", fg="black", font=(30), command=clear)
clear.grid(row=0, column=0, ipady=15, ipadx=15)

top.mainloop()
