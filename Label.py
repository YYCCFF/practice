#python
import tkinter as tk
from tkinter import font
root = tk.Tk()
root.title("Label")
root.geometry("300x300+1000+100")
label1 = tk.Label(root,text="Hello")
label1.pack(side="top")
font1 = font.Font(family="Helvetica",size=20,weight="bold")
label2 = tk.Label(root,text="Bye",bg="violet",font=font1)
label2.pack(side="top")
font2 = font.Font(family="Times",size=40)
label2 = tk.Label(root,text="See you",fg="red",font=font2)
label2.pack(side="top")
root.mainloop()
