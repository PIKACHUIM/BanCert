import os
import tkinter
import tkinter.ttk as ttk
from Modules import log
from TKPages import block
from TKPages import clean


# 清理缓存 ------------------------------------------
def cleanCache(close=True):
    logger = log.Log()
    logger.log("正在清理缓存.........", "LOG")
    os.system("rd /s/q %temp%\\ban-cert\\temp\\ 2>NUL 1>NUL")
    if close:
        viewMain.destroy()


# 主窗口创建 ----------------------------------------
if __name__ == '__main__':
    cleanCache(False)
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
    menuSub1.add_command(label='[阻止证书]更新云端源')
    menuSub1.add_command(label='[阻止证书]从本地加载')
    menuSub1.add_command(label='[阻止证书]保存到本地')
    menuSub1.add_command(label='[提交源]打开证书/EXE')
    menuSub2.add_command(label='[阻止证书]全选')
    menuSub2.add_command(label='[阻止证书]反选')
    menuSub2.add_command(label='[阻止证书]应用')
    menuSub2.add_command(label='[提交]上传证书')
    menuSub3.add_command(label='关于')
    menuSub3.add_command(label='更新')
    menuSub3.add_command(label='退出')
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
    viewMain.protocol('WM_DELETE_WINDOW', cleanCache)
    viewMain.mainloop()
