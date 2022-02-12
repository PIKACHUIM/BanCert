from tkinter import *
import tkinter
import tkinter.ttk as ttk
from pages import block
from pages import clean

# 主窗口创建 ----------------------------------------
if __name__ == '__main__':
    viewMain = tkinter.Tk()
    viewMain.geometry("600x400")
    viewMain.title("PC软件代码签名证书限制工具")
    # 创建主菜单-------------------------------------
    menuMain = tkinter.Menu(viewMain)  # 创建主菜单
    viewMain['menu'] = menuMain  # 顶级菜单关联根窗体
    # 创建子菜单-------------------------------------
    menuSub1 = tkinter.Menu(menuMain)
    menuSub2 = tkinter.Menu(menuMain)
    menuSub3 = tkinter.Menu(menuMain)
    # 子菜单栏---------------------------------------
    menuSub1.add_command(label='打开')
    menuSub1.add_command(label='保存')
    menuSub2.add_command(label='复制')
    menuSub2.add_command(label='删除')
    menuSub3.add_command(label='关于')
    # 创建顶级菜单栏，并关联子菜单---------------------
    menuMain.add_cascade(label='文件', menu=menuSub1)
    menuMain.add_cascade(label='编辑', menu=menuSub2)
    menuMain.add_cascade(label='关于', menu=menuSub3)
    # 子标签页面 ---------------------------------------------
    tabMain = ttk.Notebook()  # 创建分页栏
    tabMain.place(relx=0, rely=0, relwidth=1, relheight=0.96)
    # 将页插入分页栏中 ----------------------------------------
    tabBlock = block.Block(tabMain)
    tabClean = clean.Clean(tabMain)
    tabMain.add(tabBlock.tab(tabMain), text='阻止运行（禁用不受欢迎的软件）')
    tabMain.add(tabClean.tab(tabMain), text='证书提交（向服务器举报不受欢迎的软件证书）')
    # 进入主消息循环 ------------------------------------------
    viewMain.mainloop()
