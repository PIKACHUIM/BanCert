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
            if obj[loop_main] == "\n":
                loop_main = loop_main + 1
                break
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
    temp_text = info.replace(" ", "").replace("\t", "")
    if len(temp_text) > 0:
        return "[" + time_text + "][" + status[level] + "][" + mod + "]" + temp_text
    else:
        return None


class Log:
    # 构造方法 ------------------
    def __init__(self, box=None):
        self.box = box

    # 调试输出 -------------------------------------------------
    def log(self,
            info="---------------------",  # 消息内容
            # 模块编号 事件等级  分割长度  保留换行符
            mod="MSG", level=0,  lens=21, line=True,
            # 控制台输出 文件输出  文件输出的存储路径
            console=True, file=True, path="%temp%\\ban-cert\\"):

        # 窗口内部输出 ---------------------------------------
        data_text = cut(info, lens)
        for item in data_text:
            main_text = dat(item.replace(" ", ""), mod, level)
            if self.box is not None and main_text is not None:
                self.box.configure(state='normal')
                self.box.insert(INSERT, main_text + "\n")
                self.box.see("end")
                self.box.configure(state='disabled')
        full_logs = dat(info, mod, level)
        # 控制台和文件输出 -----------------------------------
        if full_logs is not None:
            # 输出换行控制 ------------------------------
            if line:
                full_logs = full_logs.replace("\n", "")
            # 命令行输出 --------------------------------
            if console:
                print(full_logs + "\n", end="")
            # 文件输出 ----------------------------------
            if file:
                path_logs = "echo " + path
                path_logs = os.popen(path_logs).read()
                path_logs = path_logs.replace("\n", "")
                if not os.path.exists(path_logs):
                    os.popen("mkdir " + path_logs).read()
                path_logs = path_logs + "log.txt"
                with open(path_logs, "a") as file:
                    file.write(full_logs)
            # 返回完整信息 ------------------------------
            return full_logs
