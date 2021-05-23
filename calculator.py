from tkinter import *
from binary import binary
from hexa import hexa
from Octa import octa
from PIL import ImageTk
from main_convertor import area, length, volume



top = Tk()
top.title('Calculator')
top.iconbitmap('cal.ico')

#Entry
entry = Entry(top, width=35, borderwidth=5)
entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

def button_click(num):
  current = entry.get()
  entry.delete(0, END)
  entry.insert(0, str(current) + str(num))

def clear():
  entry.delete(0, END)

def adding():
  first = entry.get()
  global f_num
  global math
  math = 'addition'
  f_num = float(first)
  entry.delete(0, END)

def button_equal():
  second = entry.get()
  entry.delete(0, END)
  if math == 'addition':
      entry.insert(0, f_num + float(second))
  if math == 'subtraction':
      entry.insert(0, f_num - float(second))
  if math == 'multiplication':
      entry.insert(0, f_num * float(second))
  if math == 'division':
      entry.insert(0, f_num / float(second))

def subtract():
  first = entry.get()
  global f_num
  global math
  math = 'subtraction'
  f_num = float(first)
  entry.delete(0, END)

def multiply():
  first = entry.get()
  global f_num
  global math
  math = 'multiplication'
  f_num = float(first)
  entry.delete(0, END)

def divide():
  first = entry.get()
  global f_num
  global math
  math = 'division'
  f_num = float(first)
  entry.delete(0, END)

def dot():
  current1 = entry.get()
  entry.delete(0, END)
  entry.insert(0, str(current1) + '.')

def dlee():
  entry.delete(len(entry.get()) - 1, len(entry.get()))

def binary1():
  binary()

def unit():
  top1 = Tk()
  top1.iconbitmap('cal.ico')
  top1.title("Unit Convertor")

def cb():
  top = Toplevel()
  image = ImageTk.PhotoImage(file = 'pictures\\area.png')
  image2 = ImageTk.PhotoImage(file='pictures\\length.png')
  image3 = ImageTk.PhotoImage(file='pictures\\volume.png')
  b1 = Button(top,image= image, command=area).grid(row=0, column=0)
  b2 = Button(top, image=image2, command=length).grid(row=0, column=1)
  b3 = Button(top, image=image3, command=volume).grid(row=0, column=2)
  top.mainloop()

def color(col):
  if col == 'red':
    top.config(bg='red')
    entry.config(bg='pink')
    b1.config(bg='pink')
    b2.config(bg='pink')
    b3.config(bg='pink')
    b4.config(bg='pink')
    b5.config(bg='pink')
    b6.config(bg='pink')
    b7.config(bg='pink')
    b8.config(bg='pink')
    b9.config(bg='pink')
    b0.config(bg='pink')
    plus.config(bg='pink')
    minus.config(bg='pink')
    multi.config(bg='pink')
    div.config(bg='pink')
    clear.config(bg='pink')
    dot.config(bg='pink')
    equal.config(bg='pink')
    delete.config(bg='pink')
    menu.config(bg='pink')
    menu2.config(bg='pink')
    menu3.config(bg='pink')
    ut.config(bg='pink')
  elif col == 'white':
    top.config(bg='white')
    entry.config(bg='white')
    b1.config(bg='white')
    b2.config(bg='white')
    b3.config(bg='white')
    b4.config(bg='white')
    b5.config(bg='white')
    b6.config(bg='white')
    b7.config(bg='white')
    b8.config(bg='white')
    b9.config(bg='white')
    b0.config(bg='white')
    plus.config(bg='white')
    minus.config(bg='white')
    multi.config(bg='white')
    div.config(bg='white')
    clear.config(bg='white')
    dot.config(bg='white')
    equal.config(bg='white')
    delete.config(bg='white')
    menu.config(bg='white')
    menu2.config(bg='white')
    menu3.config(bg='white')
    ut.config(bg='white')
  elif col == 'blue':
    top.config(bg='dark blue')
    entry.config(bg='light blue')
    b1.config(bg='light blue')
    b2.config(bg='light blue')
    b3.config(bg='light blue')
    b4.config(bg='light blue')
    b5.config(bg='light blue')
    b6.config(bg='light blue')
    b7.config(bg='light blue')
    b8.config(bg='light blue')
    b9.config(bg='light blue')
    b0.config(bg='light blue')
    plus.config(bg='light blue')
    minus.config(bg='light blue')
    multi.config(bg='light blue')
    div.config(bg='light blue')
    clear.config(bg='light blue')
    dot.config(bg='light blue')
    equal.config(bg='light blue')
    delete.config(bg='light blue')
    menu.config(bg='light blue')
    menu2.config(bg='light blue')
    menu3.config(bg='light blue')
    ut.config(bg='light blue')
  elif col == 'yellow':
    top.config(bg='yellow')
    entry.config(bg='light yellow')
    b1.config(bg='light yellow')
    b2.config(bg='light yellow')
    b3.config(bg='light yellow')
    b4.config(bg='light yellow')
    b5.config(bg='light yellow')
    b6.config(bg='light yellow')
    b7.config(bg='light yellow')
    b8.config(bg='light yellow')
    b9.config(bg='light yellow')
    b0.config(bg='light yellow')
    plus.config(bg='light yellow')
    minus.config(bg='light yellow')
    multi.config(bg='light yellow')
    div.config(bg='light yellow')
    clear.config(bg='light yellow')
    dot.config(bg='light yellow')
    equal.config(bg='light yellow')
    delete.config(bg='light yellow')
    menu.config(bg='light yellow')
    menu2.config(bg='light yellow')
    menu3.config(bg='light yellow')
    ut.config(bg='light yellow')
  elif col == 'lime':
    top.config(bg='green')
    entry.config(bg='light green')
    b1.config(bg='lime')
    b2.config(bg='lime')
    b3.config(bg='lime')
    b4.config(bg='lime')
    b5.config(bg='lime')
    b6.config(bg='lime')
    b7.config(bg='lime')
    b8.config(bg='lime')
    b9.config(bg='lime')
    b0.config(bg='lime')
    plus.config(bg='lime')
    minus.config(bg='lime')
    multi.config(bg='lime')
    div.config(bg='lime')
    clear.config(bg='lime')
    dot.config(bg='lime')
    equal.config(bg='lime')
    delete.config(bg='lime')
    menu.config(bg='lime')
    menu2.config(bg='lime')
    menu3.config(bg='lime')
    ut.config(bg='lime')


pic = ImageTk.PhotoImage(file = 'pictures\\red.png')
pic1 = ImageTk.PhotoImage(file = 'pictures\\white.png')
pic2 = ImageTk.PhotoImage(file = 'pictures\\blue.png')
pic3 = ImageTk.PhotoImage(file = 'pictures\\yellow.png')
pic4 = ImageTk.PhotoImage(file = 'pictures\\lime.png')


b1 = Button(top, text='1', padx=40, pady=20, command= lambda: button_click(1))
b2 = Button(top, text='2', padx=40, pady=20, command= lambda: button_click(2))
b3 = Button(top, text='3', padx=40, pady=20, command= lambda: button_click(3))
b4 = Button(top, text='4', padx=40, pady=20, command= lambda: button_click(4))
b5 = Button(top, text='5', padx=40, pady=20, command= lambda: button_click(5))
b6 = Button(top, text='6', padx=40, pady=20, command= lambda: button_click(6))
b7 = Button(top, text='7', padx=40, pady=20, command= lambda: button_click(7))
b8 = Button(top, text='8', padx=40, pady=20, command= lambda: button_click(8))
b9 = Button(top, text='9', padx=40, pady=20, command= lambda: button_click(9))
b0 = Button(top, text='0', padx=90, pady=20, command= lambda: button_click(0))
plus = Button(top, text='+', padx=83, pady=20, command= adding)
minus = Button(top, text='-', padx=40, pady=20, command=subtract)
multi = Button(top, text='x', padx=40, pady=20, command=multiply)
div = Button(top, text='÷', padx=40, pady=20, command=divide)
clear = Button(top, text='Clear', padx=80, pady=20, command= clear)
dot = Button(top, text='.', padx=40, pady=20, command=dot)
equal = Button(top, text='=', padx=83, pady=20, command= button_equal)
delete = Button(top, text='Del', padx=35, pady=20, command=dlee)
menu = Button(top, text='Binary Calculator', command=binary1, padx=40, pady=20)
menu2 = Button(top, text='Hexa Calculator', command=hexa, padx=44, pady=20)
menu3 = Button(top, text='Octa Calculator', command=octa, padx=44, pady=20)
ut = Button(top, text="Unit Convertor", command= cb, padx=46, pady=20)
red = Button(top, image=pic, command= lambda : color("red")).grid(row=4, column=4)
white = Button(top, image=pic1, command= lambda : color("white")).grid(row=0, column=4)
blue = Button(top, image=pic2, command= lambda : color("blue")).grid(row=1, column=4)
yellow = Button(top, image=pic3, command= lambda : color("yellow")).grid(row=2, column=4)
lime = Button(top, image=pic4, command= lambda : color("lime")).grid(row=3, column=4)


#Arranging
ut.grid(row=3, column=0)
menu2.grid(row=1, column=0)
menu3.grid(row=2, column=0)
b1.grid(row = 1, column = 1)
b2.grid(row = 1, column = 2)
b3.grid(row = 1, column = 3)
b4.grid(row = 2, column = 1)
b5.grid(row = 2, column = 2)
b6.grid(row = 2, column = 3)
b7.grid(row = 3, column = 1)
b8.grid(row = 3, column = 2)
b9.grid(row = 3, column = 3)
clear.grid(row = 6, column = 1, columnspan = 2)
dot.grid(row = 4, column = 1)
plus.grid(row=5, column=0)
minus.grid(row=5, column=1)
div.grid(row=5, column=2)
multi.grid(row=5, column=3)
equal.grid(row=6, column=0)
b0.grid(row=4, column=2, columnspan=2)
delete.grid(row=6, column=3)
menu.grid(row=0, column=0)

top.mainloop()