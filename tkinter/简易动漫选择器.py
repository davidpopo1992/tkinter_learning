# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:24:00 2022

@author: davidpopo
"""

import tkinter as tk

window=tk.Tk()
window.title('食物清单')
window.geometry('300x450')

var=tk.IntVar()


l=tk.Label(window,bg='yellow',text='请选择动漫年份',width=20)
l.pack()

acg_dict={1:'从零开始的异世界生活',2:'转生成蜘蛛又怎样',3:'女警反击'}

def printselect():
    l.config(text=acg_dict[var.get()])
    
op1=tk.Radiobutton(window,text='2020',variable=var,value=1,command=printselect)
op1.pack()

op2=tk.Radiobutton(window,text='2021',variable=var,value=2,command=printselect)
op2.pack()

op3=tk.Radiobutton(window,text='2022',variable=var,value=3,command=printselect)
op3.pack()

window.mainloop()