from tkinter import *
import tkinter.ttk as ttk


class Block:
    @staticmethod
    def tab(tabMain):
        view = Frame(tabMain)
        view.place(x=0, y=30)
        tips = Label(view, text="证书源: ")
        tips.place(x=4, y=9)
        text = Entry(view, bd=3, width=60)
        text.insert(0, "url")
        text.place(x=60, y=9)
        button_update = Button(view, text='获取证书列表', width=11)
        button_update.place(x=500, y=5)
        data = Listbox(view, width=83)
        data.place(x=5, y=50)
        show = ttk.Progressbar(view, length=585)
        show.place(x=5, y=240)
        show['maximum'] = 100  # 进度值最大值
        show['value'] = 0  # 进度值初始值
        button_all = Button(view, text='全选', width=8)
        button_all.place(x=5, y=280)
        button_not = Button(view, text='反选', width=8)
        button_not.place(x=90, y=280)
        button_exe = Button(view, text='禁止所选证书', width=20)
        button_exe.place(x=5, y=320)
        text_logs = Text(view, width=59, height=5)
        text_logs.place(x=172, y=280)
        text_logs.insert(INSERT, '')
        return view


"""
        for item in ['公鸡', '母鸡', '小鸡', '火鸡', '战斗机', ]:
            theLB.insert(END, item)  # END表示每插入一个都是在最后一个位置
"""
