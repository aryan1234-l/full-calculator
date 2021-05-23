from tkinter import *
from tkinter import StringVar
def binary():
    def b_click(num1):
        if entry1['state'] == 'normal':
            currentx = entry1.get()
            entry1.delete(0, END)
            zn = str(currentx) + str(num1)
            entry1.insert(0, zn)
            entry2.delete(0, END)
            ans = bin(int(zn))
            entry2.insert(0, ans[2:])
        if entry1['state'] == 'disabled':
            currentx = entry2.get()
            entry2.delete(0, END)
            zn = str(currentx) + str(num1)
            entry2.insert(0, zn)

    def dlee():
        if entry1['state'] == 'normal':
            entry1.delete(len(entry1.get()) - 1, len(entry1.get()))
            bh = bin(int(entry1.get()))
            entry2.delete(0, END)
            entry2.insert(0, bh[2:])
        elif entry1['state'] == 'disabled':
            entry2.delete(len(entry2.get()) - 1, len(entry2.get()))


    def clear_en():
        entry1.delete(0, END)
        entry2.delete(0, END)
        mystr.set("")

    def ad():
        if entry1['state'] == 'normal':
            first = entry1.get()
            global secondary
            global math
            math = 'addition'
            secondary = float(first)
            entry1.delete(0, END)
        if entry1['state'] == 'disabled':
            first = entry2.get()
            math = 'addition'
            secondary = int(first, 2)
            entry2.delete(0, END)

    def divide():
        if entry1['state'] == 'normal':
            first = entry1.get()
            global secondary
            global math
            math = 'division'
            secondary = float(first)
            entry1.delete(0, END)
        if entry1['state'] == 'disabled':
            first = entry2.get()
            math = 'division'
            secondary = int(first, 2)
            entry2.delete(0, END)


    def subc():
        if entry1['state'] == 'normal':
            first = entry1.get()
            global secondary
            global math
            math = 'subtraction'
            secondary = float(first)
            entry1.delete(0, END)
        if entry1['state'] == 'disabled':
            first = entry2.get()
            math = 'subtraction'
            secondary = int(first, 2)
            entry2.delete(0, END)

    def multipl():
        if entry1['state'] == 'normal':
            first = entry1.get()
            global secondary
            global math
            math = 'multiplication'
            secondary = float(first)
            entry1.delete(0, END)
        if entry1['state'] == 'disabled':
            first = entry2.get()
            math = 'multiplication'
            secondary = int(first, 2)
            entry2.delete(0, END)

    def to_dec(m):
        return int(m, 2)


    def button_equal():
        if entry1['state'] == "normal":

            second = entry1.get()
            entry1.delete(0, END)
            if math == 'addition':
                w = secondary + float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
            if math == 'subtraction':
                w = secondary - float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
            if math == 'multiplication':
                w = secondary * float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
            if math == 'division':
                w = secondary / float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
        if entry1['state'] == 'disabled':
            if math == 'addition':
                second = int(entry2.get(), 2)
                w = secondary + second
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
                mystr.set(str(w))
            if math == 'subtraction':
                second = int(entry2.get(), 2)
                w = secondary - second
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
                mystr.set(str(w))
            if math == 'multiplication':
                second = int(entry2.get(), 2)
                w = secondary * second
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
                mystr.set(str(w))
            if math == 'division':
                second = int(entry2.get(), 2)
                w = secondary / second
                entry2.delete(0, END)
                entry2.insert(0, bin(int(w))[2:])
                mystr.set(str(w))






    def for_b1():
        n2['state'] = "normal"
        n3['state'] = "normal"
        n4['state'] = "normal"
        n5['state'] = "normal"
        n6['state'] = "normal"
        n7['state'] = "normal"
        n8['state'] = "normal"
        n9['state'] = "normal"
        dot['state'] = 'normal'
        entry1['state'] = "normal"

    def for_b2():
        n2['state'] = "disabled"
        n3['state'] = "disabled"
        n4['state'] = "disabled"
        n5['state'] = "disabled"
        n6['state'] = "disabled"
        n7['state'] = "disabled"
        n8['state'] = "disabled"
        n9['state'] = "disabled"
        dot['state'] = 'disabled'
        entry1['state'] = "disabled"

    def dot():
        strs = str(entry1.get())
        entry1.delete(0, END)
        entry1.insert(0, strs + '.')


    top = Tk()
    top.title("Binary Calculator")
    top.iconbitmap('cal.ico')
    mystr = StringVar()

    entry1 = Entry(top, textvariable=mystr, width=35, borderwidth=5)
    entry2 = Entry(top, width=35, borderwidth=5)

    #Buttons
    b1 = Button(top, text='Decimal', padx=10, command=for_b1)
    b2 = Button(top, text='Binary', padx=15, command=for_b2)
    plus = Button(top, text='+', padx=27, pady=20, command=ad)
    minus = Button(top, text='-', padx=27, pady=20, command=subc)
    multi = Button(top, text='*', padx=27, pady=20, command=multipl)
    div = Button(top, text='÷', padx=27, pady=20, command=divide)
    n1 = Button(top, text='1', padx=47, pady=20, command= lambda: b_click(1))
    n2 = Button(top, text='2', padx=47, pady=20, command= lambda: b_click(2))
    n3 = Button(top, text='3', padx=47, pady=20, command= lambda: b_click(3))
    n4 = Button(top, text='4', padx=47, pady=20, command= lambda: b_click(4))
    n5 = Button(top, text='5', padx=47, pady=20, command= lambda: b_click(5))
    n6 = Button(top, text='6', padx=47, pady=20, command= lambda: b_click(6))
    n7 = Button(top, text='7', padx=47, pady=20, command= lambda: b_click(7))
    n8 = Button(top, text='8', padx=47, pady=20, command= lambda: b_click(8))
    n9 = Button(top, text='9', padx=47, pady=20, command= lambda: b_click(9))
    n0 = Button(top, text='0', padx=47, pady=20, command= lambda: b_click(0))
    dot = Button(top, text='.', padx=29, pady=20, command=dot)
    equal = Button(top, text='=', padx=52, pady=52, command=button_equal)
    dele = Button(top, text='Del', padx=47, pady=52, command = dlee)
    clear = Button(top, text='Clear', padx=42, pady=20, command=clear_en)

    dot.grid(row=6, column=0)
    dele.grid(row=4, column=3, rowspan=2)
    equal.grid(row=2, column=3, rowspan=2)
    clear.grid(row=6, column=3)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)
    n1.grid(row=2, column=1)
    n0.grid(row=2, column=2)
    n2.grid(row=3, column=1)
    n3.grid(row=3, column=2)
    n4.grid(row=4, column=1)
    n5.grid(row=4, column=2)
    n6.grid(row=5, column=1)
    n7.grid(row=5, column=2)
    n8.grid(row=6, column=1)
    n9.grid(row=6, column=2)
    plus.grid(row=2, column=0)
    minus.grid(row=3, column=0)
    multi.grid(row=4, column=0)
    div.grid(row=5, column=0)
    entry1.grid(row=0, column=1, columnspan=2)
    entry2.grid(row=1, column=1, columnspan=2)
    top.mainloop()

