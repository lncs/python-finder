# coding=utf-8
import os
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import tkinter.filedialog as tkFileDialog
import find as find

from logpublic import *
# from icon import img


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window):
    return window.winfo_reqwidth(), window.winfo_reqheight()


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    # print(size)
    root.geometry(size)


def select_dir():

    # dirPath = tkFileDialog.askopenfilename(filetypes=[("files","*.xlsx;*.xls")], initialdir = './')
    dir_path = tkFileDialog.askdirectory()

    DirPath.set(dir_path)
    show_files(DirPath.get())


def cmd():
    try:
        app_logger.info("开始运行查询程序...")
        find.find(DirPath.get(), FileSuffix.get(), Content.get())
        show_result()
        app_logger.info("查询程序运行完成...")
    except Exception as e:
        app_logger.error("程序运行出现异常:{}".format(e))
        scrtext.config(state='normal')
        scrtext.delete(1.0, END)
        scrtext.insert(END, r"ERROR:" + str(e))
        scrtext.config(state='disabled')


def show_result():
    scrtext.config(state='normal')
    scrtext.delete(1.0, END)
    scrtext.update()
    scrtext.see(END)

    f = open('result.txt', 'r+', encoding='utf-8')
    if os.path.getsize('result.txt'):
        while 1:
            text = f.readline()
            scrtext.insert(END, text)
            scrtext.see(END)
            scrtext.focus_force()
            scrtext.update()
            if not text:
                break
    else:
        scrtext.insert(END, r"不存在以[" + FileSuffix.get() + r"]为后缀的文件，或该后缀文件中没有包含[" + Content.get() + "]内容的行")
    f.close()
    scrtext.config(state='disabled')


def show_files(path):
    scrtext.config(state='normal')
    scrtext.delete(1.0, END)
    scrtext.update()

    for root, dirs, files in os.walk(path):
        for name in files:
            scrtext.insert(END, name + '\n')
    scrtext.config(state='disabled')


root = Tk()
# 导入icon.py中的img, 创建一个临时的tmp.ico文件作为图标引入后删除
# tmp = open("tmp.ico","wb+")
# tmp.write(base64.b64decode(img))
# tmp.close()
# root.iconbitmap("tmp.ico")
# os.remove("tmp.ico")

# root.iconbitmap('icon.ico')

root.title('Finder(V1.2_20190613)')

center_window(root, 800, 500)
root.resizable(False, False)
root.maxsize(800, 500)
root.minsize(600, 440)

# 文件夹路径
DirPath = StringVar()
# 文件后缀名
FileSuffix = StringVar()
# 查询内容
Content = StringVar()
# 编码格式
EncodingFormat = StringVar()

dirLabel = Label(root, text="文件路径：")
dirEntry = Entry(root, textvariable=DirPath)
dirEntry.bind("<KeyPress>", lambda e: "break")
btnselectDir = Button(root, text="浏览", command=select_dir)

suffixLabel = Label(root, text="文件后缀：")
suffixEntry = Entry(root, textvariable=FileSuffix)
# suffixEntry.bind("<KeyPress>", lambda e : "break")

# formatLabel = Label(root, text="编码：")
# formatChosen = ttk.Combobox(root, width=12, textvariable=EncodingFormat, state='readonly')
# formatChosen['values'] = ('gbk', 'utf-8')     # 设置下拉列表的值
# formatChosen.grid(column=1, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
# formatChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值


contentLabel = Label(root, text="查询内容：")
contentEntry = Entry(root, textvariable=Content)
# contentEntry.bind("<KeyPress>", lambda e : "break")

scrolW = 600  # 设置文本框的长度
scrolH = 350  # 设置文本框的高度
scrtext = ScrolledText(root, width=scrolW, height=scrolH)
# scrtext.bind("<KeyPress>", lambda e : "break")

copyRightLabel = Label(root, text="技术支持：ln8429@163.com")

btnstart = Button(root, text="查询", command=cmd)

dirLabel.place(x=5, y=10, width=100, height=25)
dirEntry.place(x=100, y=10, width=580, height=25)
btnselectDir.place(x=720, y=10, width=50, height=25)

suffixLabel.place(x=5, y=50, width=100, height=25)
suffixEntry.place(x=100, y=50, width=100, height=25)

# formatLabel.place(x=210, y=50, width=40, height=25)
# formatChosen.place(x=250, y=50, width=50, height=25)

contentLabel.place(x=210, y=50, width=100, height=25)
contentEntry.place(x=300, y=50, width=380, height=25)


btnstart.place(x=720, y=50, width=50, height=25)
scrtext.place(x=10, y=90, width=780, height=390)
copyRightLabel.place(x=490, y=480, width=400, height=25)
mainloop()
