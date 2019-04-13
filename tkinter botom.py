# -*- coding: utf-8 -*-
#python
import tkinter as tk

def pushed(self):
    self["text"]="押されたよ"

root = tk.Tk()
root.geometry("320x240")
root.title("tkinter test")

label = tk.Label(root,text="Tkinterのテストです")
label.grid()

button = tk.Button(root, text="ボタン", command= lambda : pushed(button))
button.pack()

root.mainloop()
