# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 21:52:00 2022

@author: davidpopo
"""

import tkinter as tk
import json
import datetime
import os

window=tk.Tk()
window.title('签到器')
window.geometry('300x150')


#用于记录签到天数
with open('sign_days.json') as f:
    sign_days=json.load(f)

var=tk.StringVar()
var.set('签到天数:%d'%sign_days)


#l=tk.Label(window,textvariable=var,bg='#99CC99',font=('微软雅黑',8),width=30,height=5)
l=tk.Label(window,textvariable=var,bg='#99CC99',font=('微软雅黑',8),width=30,height=5)
l.pack()

#判断今天是否签到
from sign_days_log import sign_log

date_td=datetime.datetime.now().strftime('%Y%m%d')
log_file='signdays_'+date_td+'.json'
sign_log()

with open(r'sign_log/%s'%log_file) as f:
    if_click=json.load(f)
  


def sign_in():
    global if_click
    global sign_days
    if if_click==0:        
        if_click=1
        sign_days+=1
        var.set('签到天数:%d'%sign_days)
        with open('sign_days.json','w') as f:
            json.dump(sign_days,f)
        with open(r'sign_log/%s'%log_file,'w') as f:
            json.dump(if_click,f)
    else:
        pass
        
        
b=tk.Button(window,text='点击签到',bg='#FFFFCC',font=('微软雅黑',6),width=15,height=3,command=sign_in)
b.pack()

window.mainloop()