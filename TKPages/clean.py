import hashlib
import json
import os
import string
import time
import tkinter.messagebox
from random import random
from tkinter import *

import requests
from TKPages import views
from Modules import log
from Modules import add
import tkinter.ttk as ttk
import tkinter.filedialog as fdl


class Clean(views.View):
    def __init__(self, tabRoot):
        super(Clean, self).__init__(tabRoot)
        # 证书内容变量 ------
        self.certs_path = ""  # 证书路径
        self.option_dat = None
        self.option_cp6 = None
        self.option_cp5 = None
        self.option_cp4 = None
        self.option_cp3 = None
        self.option_cp2 = None
        self.option_cp1 = None
        self.texts_hash = StringVar()
        self.texts_exts = StringVar()
        self.texts_uses = StringVar()
        self.texts_ends = StringVar()
        self.texts_star = StringVar()
        self.texts_last = StringVar()
        self.texts_sgin = StringVar()
        self.texts_ency = StringVar()
        self.texts_vers = StringVar()
        self.texts_crid = StringVar()
        self.texts_orgs = StringVar()
        self.texts_name = StringVar()
        # 证书内容标签 -------
        self.certc_hash = None
        self.certc_exts = None
        self.certc_uses = None
        self.certc_ends = None
        self.certc_star = None
        self.certc_last = None
        self.certc_sgin = None
        self.certc_ency = None
        self.certc_vers = None
        self.certc_crid = None
        self.certc_orgs = None
        self.certc_name = None
        # 证书固定文本 -------
        self.text_links = None
        self.text_links_text = StringVar()
        self.certs_ends = None
        self.certs_hash = None
        self.certs_exts = None
        self.certs_uses = None
        self.certs_star = None
        self.certs_orgs = None
        self.certs_last = None
        self.certs_vers = None
        self.certs_sgin = None
        self.certs_ency = None
        self.certs_crid = None
        self.certs_name = None
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
        # 调试器 -------------
        self.log = None

    # 打开文件 ----------------
    def action_get(self):
        file_path = fdl.askopenfilename()
        self.log.log(file_path)
        self.text_files.delete(0, END)
        self.text_files.insert(0, file_path)

    # 分析文件 ----------------
    def action_add(self):
        file_path = self.text_files.get()
        file_type = file_path[-3:]
        if file_type == "exe":
            hashtp = hashlib.sha1(str(time.time()).encode("ASCII"))
            radoms = ''.join(hashtp.hexdigest())
            pathtp = "%temp%\\ban-cert\\temp\\" + radoms + "\\"
            self.log.log("地址:" + pathtp, "ADD")
            result = os.popen("mkdir " + pathtp).read()
            self.log.log(result)
            result = os.popen("copy /y Binrary\\cert.exe " + pathtp).read()
            self.log.log(result)
            result = os.popen("copy /y Binrary\\run.bat " + pathtp).read()
            self.log.log(result)
            result = os.popen("copy /y " + file_path.replace("/", "\\") + " " + pathtp + "target.exe").read()
            self.log.log(result)
            result = os.popen(pathtp + "run.bat").read()
            self.log.log(result)
            result = os.popen("echo " + pathtp).read().replace("\n", "")
            file_sets = os.listdir(result)
            for item in file_sets:
                if item[-3:] == "cer":
                    self.text_files.delete(0, END)
                    self.text_files.insert(0, result + "\\" + item + "")
        elif not file_type == "cer":
            tkinter.messagebox.showerror(title='出错了！',
                                         message='文件类型错误，请选择exe文件或者cer文件')
            return None
        try:

            file_path = self.text_files.get()
            file_path.replace("\"", "")
            file_path = "\"" + file_path + "\""
            self.certs_path = file_path
            self.log.log("路径:" + file_path, "ADD")
            file_info = add.dump(file_path)
        except IndexError:
            tkinter.messagebox.showerror(title='出错了！',
                                         message='解析遇到问题，请检查文件以及是否有签名')
            return None
        for item in file_info:
            self.log.log(item + ": " + file_info[item], "CER")
        # 配置变量 ---------------------------------------------
        self.texts_hash.set(file_info['hash'])  # 证书哈希
        self.texts_exts.set(file_info['extend'])  # 拓展用途
        self.texts_uses.set(file_info['usage'])  # 证书用途
        self.texts_ends.set(file_info['ends'])  # 到期时间
        self.texts_star.set(file_info['start'])  # 生效时间
        self.texts_last.set(file_info['supper'])  # 颁发机构
        self.texts_sgin.set(file_info['encryption'])  # 签名算法
        self.texts_ency.set(file_info['public'])  # 加密算法
        self.texts_vers.set(file_info['v'])  # 证书版本
        self.texts_crid.set(file_info['id'])  # 证书编号
        self.texts_orgs.set(file_info['org'])  # 使用组织
        self.texts_name.set(file_info['name'])  # 主体名称

    # 上传证书文件 --------------------------------------------------------------------
    def post_cert(self):
        self.log.log("路径: " + self.certs_path, "POST")
        if len(self.certs_path) == 0:
            tkinter.messagebox.showerror("请先分析", "请先‘打开’文件并点击‘分析’")
        else:
            msg = "未知错误"
            try:
                file_path = self.certs_path.replace('"', '')
                post_data = {
                    "name": self.texts_name.get(),
                    "reason": "",
                    "detail": ""
                }
                post_file = {
                    'file': (self.texts_hash.get(), open(file_path, 'rb')),
                    'data': json.dumps(post_data)
                }

                self.log.log("地址: " + self.text_links_text.get(), "POST")
                post_rets = requests.post(self.text_links_text.get(),
                                          files=post_file)
                post_text = ""
                try:
                    post_text = json.loads(post_rets.text)
                    msg = post_text['msg']
                except json.decoder.JSONDecodeError:
                    msg = post_text
            except Exception as e:
                tkinter.messagebox.showerror("提交错误", "原因:" + str(e))
                self.log.log("错误: " + str(e), "POST")
            else:
                tkinter.messagebox.showinfo("提交完成", "返回结果:" + msg)
                self.log.log("返回: " + msg, "POST")

    def tab(self, tabMain):
        # 获取列表标签 ---------------------------------------------
        self.label_file = Label(self.view, text="exe或证书文件: ")
        self.label_file.place(x=3, y=9)
        # 获取列表链接 ---------------------------------------------
        self.text_files = Entry(self.view, bd=3, width=53)
        self.text_files.place(x=100, y=9)
        # 获取列表按钮 ---------------------------------------------
        self.button_exe = Button(self.view, text='打开', width=6,
                                 command=self.action_get)
        self.button_exe.place(x=480, y=5)
        self.button_get = Button(self.view, text='分析', width=6,
                                 command=self.action_add)
        self.button_get.place(x=540, y=5)
        # 证书信息框架 ----------------------------------------------
        self.frame_info = LabelFrame(self.view, width=415, height=200,
                                     highlightbackground='grey',
                                     text="证书信息")
        self.frame_info.place(x=5, y=35)
        # 子内容 --------------------------------------------------------
        self.certs_name = Label(self.view, text="证书:")
        self.certs_name.place(x=10, y=50)
        self.certc_name = Label(self.view, textvariable=self.texts_name)
        self.certc_name.place(x=65, y=50)
        self.certs_orgs = Label(self.view, text="主体名称内部组织:")
        self.certs_orgs.place(x=10, y=70)
        self.certc_orgs = Label(self.view, textvariable=self.texts_orgs)
        self.certc_orgs.place(x=120, y=70)
        self.certs_crid = Label(self.view, text="序列号:")
        self.certs_crid.place(x=10, y=90)
        self.certc_crid = Label(self.view, textvariable=self.texts_crid)
        self.certc_crid.place(x=60, y=90)
        self.certs_vers = Label(self.view, text="版本:")
        self.certs_vers.place(x=10, y=110)
        self.certc_vers = Label(self.view, textvariable=self.texts_vers)
        self.certc_vers.place(x=45, y=110)
        self.certs_ency = Label(self.view, text="加密算法:")
        self.certs_ency.place(x=120, y=110)
        self.certc_ency = Label(self.view, textvariable=self.texts_ency)
        self.certc_ency.place(x=175, y=110)
        self.certs_sgin = Label(self.view, text="签名算法:")
        self.certs_sgin.place(x=255, y=110)
        self.certc_sgin = Label(self.view, textvariable=self.texts_sgin)
        self.certc_sgin.place(x=310, y=110)
        self.certs_last = Label(self.view, text="颁发者:")
        self.certs_last.place(x=10, y=130)
        self.certc_last = Label(self.view, textvariable=self.texts_last)
        self.certc_last.place(x=60, y=130)
        self.certs_star = Label(self.view, text="生效于:")
        self.certs_star.place(x=10, y=150)
        self.certc_star = Label(self.view, textvariable=self.texts_star)
        self.certc_star.place(x=60, y=150)
        self.certs_ends = Label(self.view, text="失效于:")
        self.certs_ends.place(x=205, y=150)
        self.certc_ends = Label(self.view, textvariable=self.texts_ends)
        self.certc_ends.place(x=255, y=150)
        self.certs_uses = Label(self.view, text="密钥用法:")
        self.certs_uses.place(x=10, y=170)
        self.certc_uses = Label(self.view, textvariable=self.texts_uses)
        self.certc_uses.place(x=70, y=170)
        self.certs_exts = Label(self.view, text="增强型密钥用法:")
        self.certs_exts.place(x=10, y=190)
        self.certc_exts = Label(self.view, textvariable=self.texts_exts)
        self.certc_exts.place(x=110, y=190)
        self.certs_hash = Label(self.view, text="证书SHA1:")
        self.certs_hash.place(x=10, y=210)
        self.certc_hash = Label(self.view, textvariable=self.texts_hash)
        self.certc_hash.place(x=80, y=210)
        # 提交信息框架 ---------------------------------------------------
        self.frame_data = LabelFrame(self.view, width=167, height=200,
                                     highlightbackground='grey',
                                     text="提交原因")
        self.frame_data.place(x=425, y=35)
        # 提交信息内容 --------------------------------------------------------
        self.option_cp1 = Checkbutton(self.view, text="静默推广、安装其他软件")
        self.option_cp1.place(x=430, y=50)
        self.option_cp2 = Checkbutton(self.view, text="非法搜集、滥用用户隐私")
        self.option_cp2.place(x=430, y=70)
        self.option_cp3 = Checkbutton(self.view, text="弹窗广告、骚扰用户行为")
        self.option_cp3.place(x=430, y=90)
        self.option_cp4 = Checkbutton(self.view, text="病毒、蠕虫、不安全行为")
        self.option_cp4.place(x=430, y=110)
        self.option_cp5 = Checkbutton(self.view, text="篡改主页、修改搜索引擎")
        self.option_cp5.place(x=430, y=130)
        self.option_cp6 = Checkbutton(self.view, text="其他不受欢迎、流氓行为")
        self.option_cp6.place(x=430, y=150)
        self.option_dat = Text(self.view, width=21, height=2)
        self.option_dat.place(x=435, y=180)
        # 进度条 --------------------------------------------------------------
        self.processbar = ttk.Progressbar(self.view, length=587)
        self.processbar.place(x=5, y=242)
        self.processbar['maximum'] = 100  # 进度值最大值
        self.processbar['value'] = 0  # 进度值初始值
        # 调试输出窗口 ----------------------------------------------
        self.text_shows = Text(self.view, width=49, height=6)
        self.text_shows.place(x=245, y=270)
        self.text_shows.insert(INSERT, '')
        self.text_shows.configure(state='disabled')
        # 功能执行按钮 ----------------------------------------------
        self.button_put = Button(self.view, width=32, height=2,
                                 text='向指定的服务器报告此证书\n' +
                                      '为不受欢迎的应用程序证书',
                                 command=self.post_cert)
        self.button_put.place(x=5, y=303)
        # 上传列表标签 ---------------------------------------------
        self.label_file = Label(self.view, text="url:")
        self.label_file.place(x=3, y=270)
        # 上传列表链接 ---------------------------------------------
        self.text_links = Entry(self.view, bd=3, width=29, textvariable=self.text_links_text)
        self.text_links_text.set("https://sscb-us.pika.net.cn/post")
        self.text_links.place(x=28, y=270)
        # 调试内容绑定 ---------------------------------------------
        self.log = log.Log(self.text_shows)
        self.log.log()
        self.log.log("页面初始化完成!!!!!!!", "ADD")
        return self.view
