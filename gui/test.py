#!/usr/bin/env python
# coding=utf-8

import sys,time
import tkinter

top=tkinter.Tk(className='Clock')

#窗口大小
top.minsize(500, 500)


label=tkinter.Label(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
label.pack()

#def trickit():
#    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#    Label1.config(text=currentTime)
#    root.update()
#    Label1.after(1000, trickit)
#Label1.after(1000, trickit)

top.mainloop()
