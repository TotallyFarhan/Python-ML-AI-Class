from tkinter import *

tk_window = Tk()
tk_window.geometry("400x300")

tk_window.title("GUI")

def print_hello():
    print("Hello")

button = Button(text="Say Hello",command=print_hello)
button.grid(column=0,row=1)

label = Label(text="Hello There")
label.grid(column=0,row=2)


button = Button(text="Say Hello",command=print_hello)
button.grid(column=0,row=1)
