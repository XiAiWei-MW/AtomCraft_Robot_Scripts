# --Description: 使用Tkinter创建带GUI的脚本
import sys

import cri.atomcraft.criatomcraft_api_lib as acconnect
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject
import tkinter as tk
from tkinter import messagebox


def change_color():
    obj = acproject.get_selected_objects('Cue')['data']
    for item in obj:
        acproject.set_color(item, '255, 0, 0')
    return


def unset_color():
    obj = acproject.get_selected_objects('Cue')['data']
    for item in obj:
        acproject.unset_color(item)


if __name__ == '__main__':
    # 通信功能初始化
    acconnect.initialize()

    # 连接到AtomCraft
    connect_result = acconnect.connect('127.0.0.1', 9000)

    # 检测是否成功连接
    if connect_result != 0:
        print('AtomCraft connect failed')
        sys.exit(0)

    # 成功连接AtomCraft
    acdebug.log('AtomCraft remote connection success')

    # 新建Tkinter窗口并命名
    window = tk.Tk()
    window.title('Tkinter Tutorial')

    # 创建两个按钮
    button_1 = tk.Button(
        window,
        text='Change Color',
        width=20,
        height=2,
        command=change_color
    )
    button_1.grid(
        row=0,
        column=1,
        columnspan=3
    )
    button_2 = tk.Button(
        window,
        text='Unset Color',
        width=20,
        height=2,
        command=unset_color
    )
    button_2.grid(
        row=1,
        column=1,
        columnspan=3
    )

    # 窗口大小
    window.geometry("320x160")

    # 窗口置顶
    window.call('wm', 'attributes', '.', '-topmost', '1')

    # 运行窗口
    window.mainloop()
