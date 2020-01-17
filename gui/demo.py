#!/usr/bin/env python
# coding=utf-8

import tkinter

top=tkinter.Tk(className='hello world')

#窗口大小
top.minsize(500, 500)

#加标签
label=tkinter.Label(top)
label['text']='test'
label.pack()

#定义按钮功能：
def on_click():
    print('hello world!')


#添加按钮：
button=tkinter.Button(top)
button['text']='click'
button.pack()

#添加按钮操作：
button['command']=on_click
button.pack()

#添加可编辑文本框：
text=tkinter.StringVar()
text.set('Chage to what?')
entry=tkinter.Entry(top)
entry['textvariable']=text
entry.pack()

#进入消息循环体
top.mainloop()

