#!/usr/bin/env python
# coding=utf-8

import tkinter

class App:
    def __init__(self,master):
        #构造函数传入一个父组件master，创建一个Frame组件并显示.
        frame=tkinter.Frame(master)
        frame.pack()

        #创建退出按钮，并显示为红色
        self.button=tkinter.Button(frame,text='Quit',fg="red",command=frame.quit)
        self.button.pack(side=tkinter.LEFT)

        #创建hello按钮
        self.hi_there=tkinter.Button(frame,text="Hello",command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

    def say_hi(self):
        print('Hi there,this is a test.')

win=tkinter.Tk(className='Double button test.')
win.minsize(300, 300)
app=App(win)
win.mainloop()
