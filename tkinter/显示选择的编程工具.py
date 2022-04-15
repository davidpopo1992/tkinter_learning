# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:16:37 2022

@author: davidpopo
"""

import tkinter as tk

window=tk.Tk()
window.title('选择编程工具')
window.geometry('300x100')

l=tk.Label(window,bg='yellow',text='',width=20)
l.pack()

var1=tk.IntVar()
var2=tk.IntVar()

def printselect():
    if var1.get()==0 and var2.get()==0:
        l.config(text='两门语言都不喜欢')
    elif var1.get()==1 and var2.get()==0:
        l.config(text='喜欢Python')
    elif var1.get()==0 and var2.get()==1:
        l.config(text='喜欢HTML/CSS')
    elif var1.get()==1 and var2.get()==1:
        l.config(text='两门语言都喜欢')

c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=printselect)
c1.pack()

c2=tk.Checkbutton(window,text='HTML/CSS',variable=var2,onvalue=1,offvalue=0,command=printselect)
c2.pack()

window.mainloop()

