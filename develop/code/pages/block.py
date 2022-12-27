import tkinter
from tkinter import *
from tkinter import scrolledtext

import requests
from module import log
from module import ban
from module import get
from pages import views
import os
import tkinter.ttk as ttk


class Block(views.View):
    def __init__(self, tabRoot):
        super(Block, self).__init__(tabRoot)
        # 组件 ---------------
        self.text_links = None
        self.label_urls = None
        self.text_shows = None
        self.button_del = None
        self.button_not = None
        self.button_all = None
        self.processbar = None
        self.button_exe = None
        self.list_certs = None
        self.button_get = None
        # 调试器 -------------
        self.log = None
        # 动态数据 -----------
        self.path = ""

    def action_get(self):
        self.processbar['value'] = 0
        try:
            self.path = get.get(url=self.text_links.get(), log=self.log)
        except requests.exceptions.ConnectionError:
            tkinter.messagebox.showerror(title='出错了！',
                                         message='获取证书源失败，请检查网络或者修改证书源URL')
            return False
        self.processbar['value'] = 50
        if self.path is not None:
            self.list_certs.delete(0, END)
            temp_data = os.listdir(self.path)
            lens = 0
            self.processbar['value'] = 0
            for item in temp_data:
                lens = lens + 1
                self.processbar['value'] = 50 + lens * 50 / len(temp_data)
                temp_path = os.path.join(self.path, item)
                if os.path.isdir(temp_path):
                    self.list_certs.insert(END, item)  # END表示每插入一个都是在最后一个位置
                    self.log.log(item)

    def action_exe(self):
        data_path = []
        lens = 0
        self.processbar['value'] = 0
        for item in range(0, self.list_certs.size() + 1):
            lens = lens + 1
            try:
                self.processbar['value'] = lens * 100 / self.list_certs.size()
            except ZeroDivisionError:
                return False
            if self.list_certs.select_includes(item):
                data_path.append(self.list_certs.get(item))
        ban.ban_cert(self.path, data_path, self.log)

    def action_all(self):
        self.list_certs.select_set(0, END)

    def action_not(self):
        for item in range(0, self.list_certs.size()):
            if self.list_certs.select_includes(item):
                self.list_certs.select_clear(item)
            else:
                self.list_certs.select_set(item)

    def action_del(self):
        result = os.popen("cmd /c bin\\pwsh.bat").read()
        self.log.log(result) if log is not None else 1
        result = os.popen("copy /y bin\\clean.ps1 " + self.path + "\\..\\").read()
        self.log.log(result) if log is not None else 1
        result = os.popen("powershell -NonInteractive -WindowStyle Hidden -NoProfile -file "
                          + self.path + "\\..\\clean.ps1").read()
        self.log.log(result) if log is not None else 1
        self.log.log("执行完成!!!!!!!!!!!!!", "BLO")

    def tab(self, tabMain):
        # 获取列表标签 ------------------------------------
        self.label_urls = Label(self.view, text="证书源: ")
        self.label_urls.place(x=4, y=9)
        # 获取列表链接 ------------------------------------
        self.text_links = Entry(self.view, bd=3, width=60)
        self.text_links.insert(0, "https://github.com/PIKACHUIM/BanCert/raw/master/certzip/cn-all.zip")
        self.text_links.place(x=60, y=9)
        # 获取列表按钮 ------------------------------------
        self.button_get = Button(self.view, text='更新', width=11, command=self.action_get)
        self.button_get.place(x=500, y=5)
        # 列表 --------------------------------------------
        self.list_certs = Listbox(self.view, selectmode=MULTIPLE, width=83)
        self.list_certs.place(x=5, y=50)
        # 进度条 ------------------------------------------
        self.processbar = ttk.Progressbar(self.view, length=585)
        self.processbar.place(x=5, y=240)
        self.processbar['maximum'] = 100  # 进度值最大值
        self.processbar['value'] = 0  # 进度值初始值
        # 选择按钮 ------------------------------------
        self.button_all = Button(self.view, text='全选', width=8, command=self.action_all)
        self.button_all.place(x=5, y=283)
        self.button_not = Button(self.view, text='反选', width=8, command=self.action_not)
        self.button_not.place(x=90, y=283)
        # 功能执行按钮 -----------------------------------------------------------------
        self.button_exe = Button(self.view, text='一键禁止所选证书',
                                 width=20, command=self.action_exe)
        self.button_exe.place(x=5, y=317)
        self.button_del = Button(self.view, text='撤销禁止\n当前系统\n所有证书',
                                 width=8, command=self.action_del, height=3)
        self.button_del.place(x=165, y=283)
        # 调试输出窗口 -----------------------------------------------------------------
        self.text_shows = scrolledtext.ScrolledText(self.view, width=49, height=5)
        self.text_shows.place(x=240, y=280)
        self.text_shows.insert(INSERT, '')
        self.text_shows.configure(state='disabled')
        self.log = log.Log(self.text_shows)
        self.log.log()
        self.log.log("页面初始化完成!!!!!!!", "BLO")
        # 返回 ---------
        return self.view
