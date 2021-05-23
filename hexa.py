from tkinter import *
def hexa():
    top = Tk()
    top.title("Hexa decimal Calculator")
    top.iconbitmap('cal.ico')
    def dot():
        if entry1['state'] == 'normal':
            cut = entry1.get()
            entry1.delete(0, END)
            entry1.insert(0, str(cut) + '.')

    def but_clic(num):
        if entry1['state'] == 'normal':
            inte = entry1.get()
            entry1.delete(0, END)
            ans = str(inte) + str(num)
            entry1.insert(0, ans)
            entry2.delete(0, END)
            hexans = str(hex(int(ans))[2:])
            entry2.insert(0, hexans.upper())
        elif entry1['state'] == 'disabled':
            indu = entry2.get()
            entry2.delete(0, END)
            abu = str(indu) + str(num)
            entry2.insert(0, abu)
            abut = str(int(abu, 16))
            mystr.set(abut)


    def for_b1():
        a['state'] = 'disabled'
        b['state'] = 'disabled'
        c['state'] = 'disabled'
        d['state'] = 'disabled'
        e['state'] = 'disabled'
        f['state'] = 'disabled'
        entry1['state'] = 'normal'
        dot['state'] = 'normal'

    def for_b2():
        a['state'] = 'normal'
        b['state'] = 'normal'
        c['state'] = 'normal'
        d['state'] = 'normal'
        e['state'] = 'normal'
        f['state'] = 'normal'
        entry1['state'] = 'disabled'
        dot['state'] = 'disabled'

    def letter(let):
        bn = entry2.get()
        entry2.delete(0, END)
        gas = str(bn) + str(let)
        entry2.insert(0, gas)
        mystr.set(str(int(gas, 16)))


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
                ham = str(hex(int(entry1.get())))[2:]
                entry2.delete(0, END)
                entry2.insert(0, ham.upper())
            except ValueError:
                entry2.delete(0, END)
        elif entry1['state'] == 'disabled':
            try:
                entry2.delete(len(entry2.get()) - 1, END)
                ddr = str(int(entry2.get(), 16))
                mystr.set(ddr)
            except ValueError:
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
            secondary = int(first, 16)
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
            secondary = int(first, 16)
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
            secondary = int(first, 16)
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
            secondary = int(first, 16)
            entry2.delete(0, END)

    def button_equal():
        if entry1['state'] == "normal":

            second = entry1.get()
            entry1.delete(0, END)
            if math == 'addition':
                w = secondary + float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:].upper())
            if math == 'subtraction':
                w = secondary - float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:].upper())
            if math == 'multiplication':
                w = secondary * float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:].upper())
            if math == 'division':
                w = secondary / float(second)
                entry1.insert(0, w)
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:].upper())
        if entry1['state'] == 'disabled':
            if math == 'addition':
                second = int(entry2.get(), 16)
                w = secondary + second
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:])
                mystr.set(str(w).upper())
            if math == 'subtraction':
                second = int(entry2.get(), 16)
                w = secondary - second
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:])
                mystr.set(str(w).upper())
            if math == 'multiplication':
                second = int(entry2.get(), 16)
                w = secondary * second
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:])
                mystr.set(str(w).upper())
            if math == 'division':
                second = int(entry2.get(), 16)
                w = secondary / second
                entry2.delete(0, END)
                entry2.insert(0, hex(int(w))[2:])
                mystr.set(str(w).upper())

    mystr = StringVar()
    entry1 = Entry(top, textvariable=mystr, width=50, borderwidth=5)
    entry2 = Entry(top, width=50, borderwidth=5)
    b1 = Button(top, text='Decimal', padx=35, command=for_b1)
    b2 = Button(top, text='Hexa', padx=43, command=for_b2)
    equal = Button(top, text='=', padx=53, pady=12, command=button_equal)
    dot = Button(top, text='.', padx=56, pady=12, command=dot)
    plus = Button(top, text='+', padx=53, pady=12, command=ad)
    minus = Button(top, text='-', padx=54, pady=12, command=subc)
    multi = Button(top, text='*', padx=54, pady=12, command=multipl)
    division = Button(top, text='÷', padx=53, pady=12, command=divide)
    n1 = Button(top, text='1', padx=45, pady=12, command= lambda: but_clic(1))
    n2 = Button(top, text='2', padx=45, pady=12, command= lambda: but_clic(2))
    n3 = Button(top, text='3', padx=45, pady=12, command= lambda: but_clic(3))
    n4 = Button(top, text='4', padx=45, pady=12, command= lambda: but_clic(4))
    n5 = Button(top, text='5', padx=45, pady=12, command= lambda: but_clic(5))
    n6 = Button(top, text='6', padx=45, pady=12, command= lambda: but_clic(6))
    n7 = Button(top, text='7', padx=45, pady=12, command= lambda: but_clic(7))
    n8 = Button(top, text='8', padx=45, pady=12, command= lambda: but_clic(8))
    n9 = Button(top, text='9', padx=45, pady=12, command= lambda: but_clic(9))
    n0 = Button(top, text='0', padx=45, pady=12, command= lambda: but_clic(0))
    delet = Button(top, text='DEL', padx=40, pady=12, command=for_del)
    clear = Button(top, text='Clear', padx=35, pady=12, command=clear)
    a = Button(top, text='A', padx=45, pady=12, command= lambda: letter('A'), state=DISABLED)
    b = Button(top, text='B', padx=45, pady=12, command= lambda: letter('B'), state=DISABLED)
    c = Button(top, text='C', padx=45, pady=12, command= lambda: letter('C'), state=DISABLED)
    d = Button(top, text='D', padx=45, pady=12, command= lambda: letter('D'), state=DISABLED)
    e = Button(top, text='E', padx=45, pady=12, command= lambda: letter('E'), state=DISABLED)
    f = Button(top, text='F', padx=45, pady=12, command= lambda: letter('F'), state=DISABLED)

    equal.grid(row=2, column=0)
    dot.grid(row=3, column=0)
    plus.grid(row=4, column=0)
    minus.grid(row=5, column=0)
    multi.grid(row=6, column=0)
    division.grid(row=7, column=0)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)
    entry1.grid(row=0, column=1, columnspan=3)
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
    delet.grid(row=5, column=1)
    n0.grid(row=5, column=2)
    clear.grid(row=5, column=3)
    a.grid(row=6, column=1)
    b.grid(row=6, column=2)
    c.grid(row=6, column=3)
    d.grid(row=7, column=1)
    e.grid(row=7, column=2)
    f.grid(row=7, column=3)

    top.mainloop()


