#!/usr/bin/env python
# coding=utf-8

import tkinter as tk
root=tk.Tk()
root.minsize(500,300)

tk.Label(root,text='pack1',bg='red').pack()
tk.Label(root,text='pack2',bg='blue').pack()
tk.Label(root,text='pack3',bg='green').pack()

root.mainloop()
