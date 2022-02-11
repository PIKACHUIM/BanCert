# -------------------------------------
#            调试输出模块
# -------------------------------------
import os
import time
from tkinter import *

status = ["信息", "成功", "警告",
          "错误", "严重", "注意"]


def cut(obj, sec):
    data_main = []
    loop_main = 0
    while loop_main < len(obj):
        loop_subs = 0
        text_subs = ""
        while loop_subs < sec and loop_main < len(obj):
            byte_lens = 2 if ord(obj[loop_main]) > 255 else 1
            if byte_lens + loop_subs <= sec:
                loop_subs = loop_subs + byte_lens
                text_subs = text_subs + obj[loop_main]
                loop_main = loop_main + 1
            else:
                break
        data_main.append(text_subs)
    return data_main


def dat(info, mod="MSG", level=0):
    time_text = time.strftime("%y%m%d %H:%M:%S", time.localtime())
    return "[" + time_text + "][" + status[level] + "][" + mod + "}" + info


class Log:
    def __init__(self, box=None):
        self.box = box

    def log(self, info="---------------------", mod="MSG", level=0):
        data_text = cut(info, 21)
        for item in data_text:
            main_text = dat(item, mod, level)
            if self.box is not None:
                self.box.insert(INSERT, main_text + "\n")
                self.box.see("end")
        full_logs = dat(info, mod, level) + "\n"
        print(full_logs)
        path_logs = "%temp%\\ban-cert\\"
        path_logs = os.popen("echo " + path_logs).read().replace("\n", "")
        if not os.path.exists(path_logs):
            os.popen("mkdir " + path_logs).read()
        with open(path_logs + "log.txt", "a") as file:
            file.write(full_logs)
        return full_logs
