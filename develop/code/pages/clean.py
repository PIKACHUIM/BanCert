from tkinter import *
from pages import views
import tkinter.ttk as ttk


class Clean(views.View):
    def __init__(self, tabRoot):
        super(Clean, self).__init__(tabRoot)
        # 组件 ---------------
        self.frame_data = None
        self.button_put = None
        self.text_shows = None
        self.processbar = None
        self.frame_info = None
        self.button_exe = None
        self.text_files = None
        self.label_file = None
        self.button_get = None

    def tab(self, tabMain):
        # 获取列表标签 ---------------------------------------------
        self.label_file = Label(self.view, text="exe或证书文件: ")
        self.label_file.place(x=3, y=9)
        # 获取列表链接 ---------------------------------------------
        self.text_files = Entry(self.view, bd=3, width=53)
        self.text_files.insert(0, "")
        self.text_files.place(x=100, y=9)
        # 获取列表按钮 ---------------------------------------------
        self.button_exe = Button(self.view, text='打开', width=6)
        self.button_exe.place(x=480, y=5)
        self.button_get = Button(self.view, text='分析', width=6)
        self.button_get.place(x=540, y=5)
        # 证书信息框架 ----------------------------------------------
        self.frame_info = LabelFrame(self.view, width=300, height=200,
                                     highlightbackground='grey',
                                     text="证书信息")
        self.frame_info.place(x=5, y=35)
        # 提交信息框架 ----------------------------------------------
        self.frame_data = LabelFrame(self.view, width=277, height=200,
                                     highlightbackground='grey',
                                     text="提交选项")
        self.frame_data.place(x=315, y=35)
        # 进度条 ----------------------------------------------------
        self.processbar = ttk.Progressbar(self.view, length=587)
        self.processbar.place(x=5, y=242)
        self.processbar['maximum'] = 100  # 进度值最大值
        self.processbar['value'] = 0  # 进度值初始值
        # 调试输出窗口 ----------------------------------------------
        self.text_shows = Text(self.view, width=49, height=6)
        self.text_shows.place(x=245, y=270)
        self.text_shows.insert(INSERT, '')
        # 功能执行按钮 ----------------------------------------------
        self.button_put = Button(self.view, width=32, height=2,
                                 text='向指定的服务器报告此证书\n' +
                                      '为不受欢迎的应用程序证书')
        self.button_put.place(x=5, y=303)
        # 上传列表标签 ---------------------------------------------
        self.label_file = Label(self.view, text="url:")
        self.label_file.place(x=3, y=270)
        # 上传列表链接 ---------------------------------------------
        self.text_files = Entry(self.view, bd=3, width=29)
        self.text_files.insert(0, "url")
        self.text_files.place(x=28, y=270)
        return self.view
