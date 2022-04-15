# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 23:17:10 2022

@author: davidpopo
"""

import datetime
import json
import os
#根据目录上是否有日志文件判断按钮是否被按过。如果未被按过，生成一个初始化文件。
def sign_log():
    date_td=datetime.datetime.now().strftime('%Y%m%d')
    log_file='signdays_'+date_td+'.json'
    if os.path.exists(r'sign_log/%s'%log_file):
        pass
    else:
        if_click=0
        f=open(r'sign_log/%s'%log_file,'w')
        json.dump(if_click,f)