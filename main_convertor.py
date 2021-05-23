from tkinter import *
from decimal import Decimal
def area():
    top = Tk()
    top.title("Area")
    top.iconbitmap('cal.ico')
    li = ["Square kilometer",
          "Square meter",
          "Hectare"]
    def click(num):
        cc = str(entry1.get())
        entry1.delete(0, END)
        x = cc + str(num)
        entry1.insert(0, x)
        backend(x)

    def backend(x):
        t = mystr.get()
        q = mystr2.get()
        if t == "Square kilometer":
            if q == "Square kilometer":
                entry2.delete(0, END)
                entry2.insert(0, x)
            elif q == "Square meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000))
            elif q == "Hectare":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 100))
        elif t == "Square meter":
            if q == "Square meter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "Square kilometer":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.000001))
            elif q == "Hectare":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.0001))
        elif t == "Hectare":
            if q == "Hectare":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "Square meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 10000))
            elif q == "Square kilometer":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.01))

    def clear():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def delt():
        entry1.delete(len(entry1.get()) - 1, END)
        try:
          endo = entry1.get()
          backend(endo)
        except ValueError:
            entry2.delete(0, END)

    def dot():
        u = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, str(u) + ".")
    mystr = StringVar(top)
    mystr.set("Square kilometer")
    mystr2 = StringVar(top)
    mystr2.set("Square meter")
    op = OptionMenu(top, mystr, *li)
    op.config(width=15)
    entry1 = Entry(top, width=45, borderwidth=5)
    op2 = OptionMenu(top, mystr2, *li)
    op2.config(width=15)
    entry2 = Entry(top, width=45, borderwidth=5)
    n1 = Button(top, text="1", padx=40, pady=20, command= lambda: click(1))
    n2 = Button(top, text="2", padx=40, pady=20, command= lambda: click(2))
    n3 = Button(top, text="3", padx=40, pady=20, command= lambda: click(3))
    n4 = Button(top, text="4", padx=40, pady=20, command= lambda: click(4))
    n5 = Button(top, text="5", padx=40, pady=20, command= lambda: click(5))
    n6 = Button(top, text="6", padx=40, pady=20, command= lambda: click(6))
    n7 = Button(top, text="7", padx=40, pady=20, command= lambda: click(7))
    n8 = Button(top, text="8", padx=40, pady=20, command= lambda: click(8))
    n9 = Button(top, text="9", padx=40, pady=20, command= lambda: click(9))
    n0 = Button(top, text="0", padx=40, pady=20, command= lambda: click(0))
    dele = Button(top, text="DEL", padx=33, pady=20, command=delt)
    clear = Button(top, text="Clear", padx=29, pady=20, command= clear)
    dot = Button(top, text=".", padx=60, pady=52, borderwidth=5, command = dot)

    op.grid(row=0, column=0)
    entry1.grid(row=0, column=1, columnspan=3)
    op2.grid(row=1, column=0)
    entry2.grid(row=1, column=1, columnspan=3)
    n1.grid(row=2, column=1)
    n2.grid(row=2, column=2)
    n3.grid(row=2, column=3)
    n4.grid(row=3, column=1)
    n5.grid(row=3, column=2)
    n6.grid(row=3, column=3)
    n7.grid(row=4, column=1)
    n8.grid(row=4, column=2)
    n9.grid(row=4, column=3)
    dele.grid(row=5, column=1)
    n0.grid(row=5, column=2)
    clear.grid(row=5, column=3)
    dot.grid(row=4, column=0, rowspan=2)

    top.mainloop()

def length():
    top = Tk()
    top.title("Length")
    top.iconbitmap('cal.ico')
    li = ["kilometer",
          "meter",
          "centimeter",
          "millimeter"]
    def click(num):
        cc = str(entry1.get())
        entry1.delete(0, END)
        x = cc + str(num)
        entry1.insert(0, x)
        backend(x)

    def backend(x):
        t = mystr.get()
        q = mystr2.get()
        if t == "kilometer":
            if q == "kilometer":
                entry2.delete(0, END)
                entry2.insert(0, x)
            elif q == "meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
            elif q == "centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 100000))
            elif q == "millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000))
        elif t == "meter":
            if q == "meter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "kilometer":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 100))
            elif q == "millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
        elif t == "centimeter":
            if q == "centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.01))
            elif q == "kilometer":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.00001))
            elif q == "millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 10))
        elif t == "millimeter":
            if q == "millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "kilometer":
                entry2.delete(0, END)
                entry2.insert(0, Decimal(str(float(x) * 0.000001)))
            elif q == "centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.1))

    def clear():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def delt():
        entry1.delete(len(entry1.get()) - 1, END)
        try:
          endo = entry1.get()
          backend(endo)
        except ValueError:
            entry2.delete(0, END)

    def dot():
        u = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, str(u) + ".")
    mystr = StringVar(top)
    mystr.set("kilometer")
    mystr2 = StringVar(top)
    mystr2.set("meter")
    op = OptionMenu(top, mystr, *li)
    op.config(width=15)
    entry1 = Entry(top, width=45, borderwidth=5)
    op2 = OptionMenu(top, mystr2, *li)
    op2.config(width=15)
    entry2 = Entry(top, width=45, borderwidth=5)
    n1 = Button(top, text="1", padx=40, pady=20, command= lambda: click(1))
    n2 = Button(top, text="2", padx=40, pady=20, command= lambda: click(2))
    n3 = Button(top, text="3", padx=40, pady=20, command= lambda: click(3))
    n4 = Button(top, text="4", padx=40, pady=20, command= lambda: click(4))
    n5 = Button(top, text="5", padx=40, pady=20, command= lambda: click(5))
    n6 = Button(top, text="6", padx=40, pady=20, command= lambda: click(6))
    n7 = Button(top, text="7", padx=40, pady=20, command= lambda: click(7))
    n8 = Button(top, text="8", padx=40, pady=20, command= lambda: click(8))
    n9 = Button(top, text="9", padx=40, pady=20, command= lambda: click(9))
    n0 = Button(top, text="0", padx=40, pady=20, command= lambda: click(0))
    dele = Button(top, text="DEL", padx=33, pady=20, command=delt)
    clear = Button(top, text="Clear", padx=29, pady=20, command= clear)
    dot = Button(top, text=".", padx=60, pady=52, borderwidth=5, command = dot)

    op.grid(row=0, column=0)
    entry1.grid(row=0, column=1, columnspan=3)
    op2.grid(row=1, column=0)
    entry2.grid(row=1, column=1, columnspan=3)
    n1.grid(row=2, column=1)
    n2.grid(row=2, column=2)
    n3.grid(row=2, column=3)
    n4.grid(row=3, column=1)
    n5.grid(row=3, column=2)
    n6.grid(row=3, column=3)
    n7.grid(row=4, column=1)
    n8.grid(row=4, column=2)
    n9.grid(row=4, column=3)
    dele.grid(row=5, column=1)
    n0.grid(row=5, column=2)
    clear.grid(row=5, column=3)
    dot.grid(row=4, column=0, rowspan=2)

    top.mainloop()

def volume():
    top = Tk()
    top.title("Volume")
    top.iconbitmap('cal.ico')
    li = ["cubic meter",
          "cubic decimeter",
          "cubic millimeter",
          "cubic centimeter",
          "Liter"]
    def click(num):
        cc = str(entry1.get())
        entry1.delete(0, END)
        x = cc + str(num)
        entry1.insert(0, x)
        backend(x)

    def backend(x):
        t = mystr.get()
        q = mystr2.get()
        if t == "cubic meter":
            if q == "cubic meter":
                entry2.delete(0, END)
                entry2.insert(0, x)
            elif q == "cubic millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000000))
            elif q == "cubic decimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
            elif q == "cubic centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000))
            elif q == "Liter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
        elif t == "cubic decimeter":
            if q == "cubic decimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "cubic millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000))
            elif q == "cubic meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "cubic centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
            elif q == "Liter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x)))
        elif t == "cubic centimeter":
            if q == "cubic centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "cubic meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.00000001))
            elif q == "cubic decimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "cubic millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
            elif q == "Liter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
        elif t == "cubic millimeter":
            if q == "cubic millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "cubic meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.000000001))
            elif q == "cubic decimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.000001))
            elif q == "cubic centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "Liter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.000001))
        elif t == "Liter":
            if q == "cubic decimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(x))
            elif q == "cubic millimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000000))
            elif q == "cubic meter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 0.001))
            elif q == "cubic centimeter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x) * 1000))
            elif q == "Liter":
                entry2.delete(0, END)
                entry2.insert(0, str(float(x)))

    def clear():
        entry1.delete(0, END)
        entry2.delete(0, END)

    def delt():
        entry1.delete(len(entry1.get()) - 1, END)
        try:
          endo = entry1.get()
          backend(endo)
        except ValueError:
            entry2.delete(0, END)

    def dot():
        u = entry1.get()
        entry1.delete(0, END)
        entry1.insert(0, str(u) + ".")
    mystr = StringVar(top)
    mystr.set("cubic meter")
    mystr2 = StringVar(top)
    mystr2.set("cubic centimeter")
    op = OptionMenu(top, mystr, *li)
    op.config(width=15)
    entry1 = Entry(top, width=45, borderwidth=5)
    op2 = OptionMenu(top, mystr2, *li)
    op2.config(width=15)
    entry2 = Entry(top, width=45, borderwidth=5)
    n1 = Button(top, text="1", padx=40, pady=20, command= lambda: click(1))
    n2 = Button(top, text="2", padx=40, pady=20, command= lambda: click(2))
    n3 = Button(top, text="3", padx=40, pady=20, command= lambda: click(3))
    n4 = Button(top, text="4", padx=40, pady=20, command= lambda: click(4))
    n5 = Button(top, text="5", padx=40, pady=20, command= lambda: click(5))
    n6 = Button(top, text="6", padx=40, pady=20, command= lambda: click(6))
    n7 = Button(top, text="7", padx=40, pady=20, command= lambda: click(7))
    n8 = Button(top, text="8", padx=40, pady=20, command= lambda: click(8))
    n9 = Button(top, text="9", padx=40, pady=20, command= lambda: click(9))
    n0 = Button(top, text="0", padx=40, pady=20, command= lambda: click(0))
    dele = Button(top, text="DEL", padx=33, pady=20, command=delt)
    clear = Button(top, text="Clear", padx=29, pady=20, command= clear)
    dot = Button(top, text=".", padx=60, pady=52, borderwidth=5, command = dot)

    op.grid(row=0, column=0)
    entry1.grid(row=0, column=1, columnspan=3)
    op2.grid(row=1, column=0)
    entry2.grid(row=1, column=1, columnspan=3)
    n1.grid(row=2, column=1)
    n2.grid(row=2, column=2)
    n3.grid(row=2, column=3)
    n4.grid(row=3, column=1)
    n5.grid(row=3, column=2)
    n6.grid(row=3, column=3)
    n7.grid(row=4, column=1)
    n8.grid(row=4, column=2)
    n9.grid(row=4, column=3)
    dele.grid(row=5, column=1)
    n0.grid(row=5, column=2)
    clear.grid(row=5, column=3)
    dot.grid(row=4, column=0, rowspan=2)

    top.mainloop()


