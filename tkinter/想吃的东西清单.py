# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:27:14 2022

@author: davidpopo
"""

import tkinter as tk

window=tk.Tk()
window.title('食物清单')
window.geometry('300x450')

def add_food():
    food=e.get()
    lb.insert('end',food)
    
def show_food():
    food_choose=lb.get(lb.curselection()) 
    var.set(food_choose)

def delete_food():
    food_delete=lb.curselection()
    try:
        lb.delete(food_delete)
    except:
        pass

#用于选择想吃的东西
l1=tk.Label(window,text='显示选择的食物',width=17,height=2)
l1.pack()

var=tk.StringVar()

l=tk.Label(window,textvariable=var,bg='white',width=17,height=2)
l.pack()

#展示选择的食物的按钮
b_show=tk.Button(window,text='显示',width=8,height=1,command=show_food)
b_show.pack()

#用于添加想吃的东西
l2=tk.Label(window,text='输入你想吃的东西',width=17,height=2)
l2.pack()
e=tk.Entry(window,show=None)
e.pack()

#添加食物的按钮
b=tk.Button(window,text='添加',width=8,height=1,command=add_food)
b.pack()

choice_var=tk.StringVar()
choice_var.set(('烤鸡蛋','土豆披萨','地三鲜'))

lb=tk.Listbox(window,listvariable=choice_var)
lb.pack()

#删除喜欢的食物
b_delete=tk.Button(window,text='删除',width=8,height=1,command=delete_food)
b_delete.pack()

window.mainloop()