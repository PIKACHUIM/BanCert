from tkinter import *


def on_resize(evt):
    tk.configure(width=evt.width, height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    print(canvas.winfo_width())


if __name__ == '__main__':
    TRANSCOLOUR = 'black'
    tk = Tk()
    tk.geometry('500x400+500+150')
    tk.title('有趣的透明窗体-开篇了！！！')
    tk.wm_attributes('-transparentcolor', TRANSCOLOUR)
    canvas = Canvas(tk)
    canvas.pack(fill=BOTH, expand=Y)
    tk.bind('<Configure>', on_resize)
    tk.mainloop()
