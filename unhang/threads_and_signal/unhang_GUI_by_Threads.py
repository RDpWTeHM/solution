#!/usr/bin/env python3


from tkinter import *
import tkinter as tk
import sys


request_pages_result = {}


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

    global request_pages_result
    sites = ("https://www.baidu.com",
             "https://www.bing.com",
             "https://www.yahoo.com",
             "http://www.so.com")

    import requests
    try:
        for site in sites:
            r = requests.get(site)
            if r.status_code != 200:
                request_pages_result[site] = False
            else:
                request_pages_result[site] = True
    except Exception as e:
        print("[Error] request_pages(): ", e, file=sys.stderr)

    show_request_pages_reslut()


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
