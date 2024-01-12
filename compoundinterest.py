from tkinter import *
from PIL import ImageTk, Image
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Compound Interest Calculator")

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\vford\OneDrive\Documents\Coding\Python\compoundinterest.jpg"))
my_label = Label(image=my_img)
my_label.grid(row =0, column=0, columnspan= 3)

def delete():
    timeinput.delete(0, END)
    compoundedinput.delete(0, END)
    rateinput.delete(0, END)
    amountinput.delete(0, END)
    label.destroy()

def calculation():
    CI = int(compoundedinput.get())
    AI = int(amountinput.get())
    RI = float(rateinput.get())
    TI = int(timeinput.get())
    interest = AI * ((1+(RI/CI))**(TI*CI))
    rounded = round(interest,2)
    label.config(text="The compound interest is: £{}". format(rounded))
    
    
amount = Label (root, text="P - Initial Investment:", font="Helvetica 11 italic")
amount.grid(row=1, column=1)

amountinput = Entry(root, width=25)
amountinput.grid(row=2,column=1)


rate = Label(root, text="r - Rate - as a decimal:", font="Helvetica 11 italic")
rate.grid(row=3, column=1)

rateinput = Entry(root, width=25)
rateinput.grid(row=4, column=1)

compounded = Label(root, text="n - Number of times the interest is compounded per year:", font="Helvetica 11 italic")
compounded.grid(row=5, column=1)

compoundedinput = Entry(root, width=25)
compoundedinput.grid(row=6, column=1)

time = Label(root, text="t - Number of years:", font="Helvetica 11 italic")
time.grid(row=7, column=1)

timeinput = Entry(root, width=25)
timeinput.grid(row=8, column=1)

whitespace = Label(root, text= " ")
whitespace.grid(row=9, rowspan=2, column=1)

    
submit = Button(root, text="Submit", command=calculation, font="Helvetica 8 bold")
reset = Button(root, text="Reset", command=delete, font="Helvetica 8 bold")
quit = Button(root, text="Exit Program", command=root.quit, font="Helvetica 8 bold")

quit.grid(row=11, column=0)
reset.grid(row=11, column=1)
submit.grid(row=11, column=2)


label = Label(root, text="The compound interest is: ", font="Helvetica 12 italic")
label.grid(row=12, column=1)

whitespace2 = Label(root, text= " ")
whitespace.grid(row=13, rowspan=2, column=1)

title = Label(root, text="Vanessa's Compound Interest Calculator")
title.grid(row=14, column=1)

root.mainloop()