#!/usr/bin/env python
# coding=utf-8

import tkinter

top=tkinter.Tk(className='hello world')

#窗口大小
#top.minsize(500, 500)

#定义按钮功能：
def on_click():
    print('hello world!')

#定义几何窗口大小，默认400*200,没有大小限制
top.geometry('400x200')

#添加按钮：
button=tkinter.Button(top)
button['text']='click'

#添加按钮操作：
button['command']=on_click
button.pack()

#进入消息循环体
top.mainloop()

