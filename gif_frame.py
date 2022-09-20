from tkinter import PhotoImage
from ttkbootstrap import Style
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from time import time
style = Style(theme="minty")
root = style.master
frameCnt = 20
t1 = time()
frames = [ttk.PhotoImage(file="hallow.gif", format='gif -index %i' % (i)) for i in range(frameCnt)]

t2 = time()
print(t2-t1)

def fun():
    c =0
    while(True):
        c += 1
        i = input()
        if c%2 == 0:
            print("theme:1")
        else:
            print("theme:2")
