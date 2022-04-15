# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:10:35 2022

@author: davidpopo
"""

import tkinter as tk
import random


window=tk.Tk()
window.title('抽奖器')
window.geometry('300x300')

prize_list=list(range(1,10))

#1个大奖
prize_level1=random.sample(prize_list,1)
print('1等奖列表',prize_level1)
prize_list=[i for i in prize_list if i not in prize_level1]

#2个中奖
prize_level2=random.sample(prize_list,2)
print('2等奖列表',prize_level2)
prize_list=[i for i in prize_list if i not in prize_level2]

#普照奖列表
prize_level3=prize_list
print('普照列表',prize_level3)


l=tk.Label(window,text='请输入1-9的数字进行抽奖',width=17,height=2)
l.pack()

e=tk.Entry(window,show=None)
e.pack()

def lottery():
    try:
        var=int(e.get())
        if var in prize_level1:
            t.insert('end','恭喜您获得1等奖\n')
        elif var in prize_level2:
            t.insert('end','恭喜您获得2等奖\n')
        elif var in prize_level3:
            t.insert('end','恭喜您获得普照奖\n')
    except:
        pass
        

b=tk.Button(window,text='点击抽奖',bg='#FFFFCC',font=('微软雅黑',6),width=8,height=3,command=lottery)
b.pack()

t=tk.Text(window,width=35)

#滚动条设置
scroll = tk.Scrollbar()
scroll.pack(side=tk.RIGHT,fill=tk.Y)
 
# 两个控件关联
scroll.config(command=t.yview)
t.config(yscrollcommand=scroll.set)
t.pack()

window.mainloop()