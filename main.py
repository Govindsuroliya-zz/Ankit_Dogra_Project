import tkinter
import os

top = tkinter.Tk()

canvas = tkinter.Canvas(top, height = 200, width=200)
canvas.pack()

def birdCallBack():
   os.system("python3 flaapy_bird-main/flaapy_bird-main/main.py")
   print("Open Flaapy Bird")

B = tkinter.Button(top, text ="Flaapy Bird", command = birdCallBack)
B.place(relx=0.5, rely=0.5, anchor="center")

B.pack(side="top")
def gameCallBack():
   print("Open Ping Pong")
   os.system("python3 gam2.py")

A = tkinter.Button(top, text ="Ping Pong", command = gameCallBack)
A.place(relx=0.5, rely=0.5, anchor="center")


A.pack()
top.mainloop()