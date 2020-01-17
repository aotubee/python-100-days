#!/usr/bin/env python
# coding=utf-8

#引入Tkinter工具包
from tkinter import *

#定义按钮功能：
def hello():
    print('hello world!')

win=Tk()
win.title('Hello world')

#定义几何窗口大小，默认400*200,没有大小限制
win.geometry('400x200')

#添加按钮：
btn=Button(win,text='click me',command=hello)

btn.pack(expand=YES,fill=BOTH)

mainloop()
