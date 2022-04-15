# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:11:14 2022

@author: davidpopo
"""

import tkinter as tk

window=tk.Tk()
window.title('每日三问')
window.geometry('300x150')

var=tk.StringVar()

l=tk.Label(window,textvariable=var,bg='#99CC99',font=('微软雅黑',8),width=30,height=5)
l.pack()

question_num=0

def question():
    global question_num
    if question_num==0:
        question_num+=1
        var.set('今天你克制坏习惯了吗')
    elif question_num==1:
        question_num+=1
        var.set('今天你好好学习了吗')
    elif question_num==2:
        question_num+=1
        var.set('今天你拓宽认知了吗')
    elif question_num==3:
        question_num=0
        var.set('')
        
        


b=tk.Button(window,text='点击自省',bg='#FFFFCC',font=('微软雅黑',6),width=15,height=3,command=question)
b.pack()



window.mainloop()


