from tkinter import *
def octa():
    top = Tk()
    top.title("Octa decimal Calculator")
    top.iconbitmap('cal.ico')
    def clear():
        if entry1['state'] == 'normal':
            entry1.delete(0, END)
            entry2.delete(0, END)
        if entry2['state'] == 'disabled':
            entry2.delete(0, END)
            mystr.set('')

    def for_del():
        if entry1['state'] == 'normal':
            try:
                entry1.delete(len(entry1.get()) - 1, len(entry1.get()))
                ham = str(oct(int(entry1.get())))[2:]
                entry2.delete(0, END)
                entry2.insert(0, ham.upper())
            except ValueError:
                entry2.delete(0, END)
        elif entry1['state'] == 'disabled':
            try:
                entry2.delete(len(entry2.get()) - 1, END)
                ddr = str(int(entry2.get(), 8))
                mystr.set(ddr)
            except ValueError:
                entry2.delete(0, END)

    def for_b1():
        n8['state'] = 'normal'
        n9['state'] = 'normal'
        entry1['state'] = 'normal'

    def for_b2():
        n8['state'] = 'disabled'
        n9['state'] = 'disabled'
        entry1['state'] = 'disabled'

    def but_clic(num):
        if entry1['state'] == 'normal':
            inte = entry1.get()
            entry1.delete(0, END)
            ans = str(inte) + str(num)
            entry1.insert(0, ans)
            entry2.delete(0, END)
            hexans = str(oct(int(ans))[2:])
            entry2.insert(0, hexans)
        elif entry1['state'] == 'disabled':
            indu = entry2.get()
            entry2.delete(0, END)
            abu = str(indu) + str(num)
            entry2.insert(0, abu)
            abut = str(int(abu, 8))
            mystr.set(abut)

    def dot():
        if entry1['state'] == 'normal':
            cut = entry1.get()
            entry1.delete(0, END)
            entry1.insert(0, str(cut) + '.')

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
            secondary = int(first, 8)
            entry2.delete(0, END)

    def subc():
        if entry1['state'] == 'normal':
            first = float(entry1.get())
            global secondary
            global math
            math = 'subtraction'
            secondary = int(first)
            entry1.delete(0, END)
        if entry1['state'] == 'disabled':
            first = entry2.get()
            math = 'subtraction'
            secondary = int(first, 8)
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
            secondary = int(first, 8)
            entry2.delete(0, END)

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
            secondary = int(first, 8)
            entry2.delete(0, END)

    def button_equal():
        if entry1['state'] == "normal":

            second = entry1.get()
            entry1.delete(0, END)
            if math == 'addition':
                w = secondary + float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
            if math == 'subtraction':
                w = secondary - float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
            if math == 'multiplication':
                w = secondary * float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
            if math == 'division':
                w = secondary / float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
        if entry1['state'] == 'disabled':
            if math == 'addition':
                second = int(entry2.get(), 8)
                w = secondary + second
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
                mystr.set(str(w))
            if math == 'subtraction':
                second = int(entry2.get(), 8)
                w = secondary - second
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
                mystr.set(str(w))
            if math == 'multiplication':
                second = int(entry2.get(), 8)
                w = secondary * second
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
                mystr.set(str(w))
            if math == 'division':
                second = int(entry2.get(), 8)
                w = secondary / second
                entry2.delete(0, END)
                entry2.insert(0, oct(int(w))[2:])
                mystr.set(str(w))


    mystr = StringVar()
    entry1 = Entry(top,textvariable= mystr, width=40, borderwidth=5)
    entry2 = Entry(top, width=40, borderwidth=5)
    decimal = Button(top, text='Decimal', padx=40, command=for_b1)
    octal = Button(top, text='Octal', padx=48, command=for_b2)
    plus = Button(top, text='+', padx = 58, pady=20, command=ad)
    minus = Button(top, text='-', padx=59, pady=20, command=subc)
    multiplication = Button(top, text='*', padx=60, pady=20, command=multipl)
    division = Button(top, text='÷', padx=58, pady=20, command=divide)
    dot = Button(top, text='.', padx=60, pady=20, command=dot)
    n1 = Button(top, text='1', padx=55, pady=20, command= lambda: but_clic(1))
    n0 = Button(top, text='0', padx=55, pady=20, command= lambda: but_clic(0))
    n2 = Button(top, text='2', padx=55, pady=20, command= lambda: but_clic(2))
    n3 = Button(top, text='3', padx=55, pady=20, command= lambda: but_clic(3))
    n4 = Button(top, text='4', padx=55, pady=20, command= lambda: but_clic(4))
    n5 = Button(top, text='5', padx=55, pady=20, command= lambda: but_clic(5))
    n6 = Button(top, text='6', padx=55, pady=20, command= lambda: but_clic(6))
    n7 = Button(top, text='7', padx=55, pady=20, command= lambda: but_clic(7))
    n8 = Button(top, text='8', padx=55, pady=20, command= lambda: but_clic(8))
    n9 = Button(top, text='9', padx=55, pady=20, command= lambda: but_clic(9))
    equal = Button(top, text='=', padx=55, pady=20, command=button_equal)
    delete = Button(top, text='DEL', padx=50, pady=53, command=for_del)
    clear = Button(top, text='Clear', padx=46, pady=52, command=clear)


    equal.grid(row=2, column=3)
    delete.grid(row=3, column=3, rowspan=2)
    clear.grid(row=5, column=3, rowspan=2)
    decimal.grid(row=0, column=0)
    octal.grid(row=1, column=0)
    entry1.grid(row=0, column=1, columnspan=2)
    entry2.grid(row=1, column=1, columnspan=2)
    plus.grid(row=2, column=0)
    minus.grid(row=3, column=0)
    multiplication.grid(row=4, column=0)
    division.grid(row=5, column=0)
    dot.grid(row=6, column=0)
    n1.grid(row=2, column=2)
    n0.grid(row=2, column=1)
    n2.grid(row=3, column=1)
    n3.grid(row=3, column=2)
    n4.grid(row=4, column=1)
    n5.grid(row=4, column=2)
    n6.grid(row=5, column=1)
    n7.grid(row=5, column=2)
    n8.grid(row=6, column=1)
    n9.grid(row=6, column=2)

    top.mainloop()

