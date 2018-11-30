#!/usr/bin/env python3


from tkinter import *
import tkinter as tk
import sys


def quit():
    print("I will quit!")
    sys.exit()


def clean():
    print("Press Clean button")
    entry.delete(0, tk.END)


def show():
    print("Press Show button")
    entry.delete(0, tk.END)
    entry.insert(0, "Button Clicked!")


def show_request_pages_reslut():
    global request_pages_result
    entry.delete(0, tk.END)
    entry.insert(0, "{!s}".format(request_pages_result))


root = Tk()
# root.pack()

win = Frame(root)
win.pack(expand=YES, fill=BOTH)

entry = Entry(win)
entry.config(text = "not clicked")
entry.pack(expand=YES, fill=BOTH)

btnShow = Button(win)
btnShow.config(text="Show", command=show)
btnShow.pack(expand=YES, fill=BOTH)

btnClean = Button(win)
btnClean.config(text="Clean", command=clean)
btnClean.pack(expand=YES, fill=BOTH)

btnQuit = Button(win)
btnQuit.config(text='Quit', command=quit)
btnQuit.pack()


root.title('unhang GUI.py')

root.mainloop()
