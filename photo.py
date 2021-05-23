from tkinter import *
from PIL import ImageTk, Image
from main_convertor import area, length, volume
def fan():

    top = Tk()
    photo = PhotoImage(file = "pictures\\area.png")

    photo2 = PhotoImage(file = "pictures\\length.png")

    photo3 = PhotoImage(file = "pictures\\length.png")

    photo4 = PhotoImage(file = "pictures\\volume.png")

    photo5 = PhotoImage(file = "pictures\\power.png")

    photo6 = PhotoImage(file = "pictures\\temp.png")

    photo7 = PhotoImage(file = "pictures\\weight.png")

    photo8 = PhotoImage(file = "pictures\\speed.png")

    photo9 = PhotoImage(file = "pictures\\press.png")

    photo10 = PhotoImage(file = "pictures\\date.png")

    photo11 = PhotoImage(file = "pictures\\age.png")

    photo12 = PhotoImage(file = "pictures\\time.png")

    def butt_cq(name):
        if name == "area":
            area()
        elif name == "length":
            length()
        elif name == "volume":
            volume()

    b1 = Button(top , padx=40, pady=20, image=photo, command=lambda: butt_cq("area"))

    b2 = Button(top , padx=40, pady=20, image=photo2, command=lambda: butt_cq("length"))

    b3 = Button(top , padx=40, pady=20, image=photo3, command=lambda: butt_cq("bmi"))

    b4 = Button(top , padx=40, pady=20, image=photo4, command=lambda: butt_cq("volume"))

    b5 = Button(top , padx=40, pady=20, image=photo5, command=lambda: butt_cq("power"))

    b6 = Button(top , padx=40, pady=20, image=photo6, command=lambda: butt_cq("temp"))

    b7 = Button(top , padx=40, pady=20, image=photo7, command=lambda: butt_cq("weight"))

    b8 = Button(top , padx=40, pady=20, image=photo8, command=lambda: butt_cq("speed"))

    b9 = Button(top , padx=40, pady=20, image=photo9, command=lambda: butt_cq("pressure"))

    b10 = Button(top , padx=40, pady=20, image=photo10, command=lambda: butt_cq("date"))

    b11 = Button(top , padx=40, pady=20, image=photo11, command=lambda: butt_cq("age"))

    b12 = Button(top , padx=40, pady=20, image=photo12, command=lambda: butt_cq("time"))


    b1.grid(row=0, column=0)

    b2.grid(row=0, column=2)

    b3.grid(row=1, column=2)

    b4.grid(row=0, column=1)

    b5.grid(row=1, column=0)

    b6.grid(row=1, column=1)

    b7.grid(row=2, column=0)

    b8.grid(row=2, column=1)

    b9.grid(row=2, column=2)

    b10.grid(row=3, column=0)

    b11.grid(row=3, column=1)

    b12.grid(row=3, column=2)

    top.mainloop()
fan()