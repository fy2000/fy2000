# -*- coding: utf-8 -*-
# 1.导入GUI库
import PySimpleGUI as sg

# 2.定义布局，定义行数
layout = [
    [],
    [],
    []
]

if __name__ == '__main__':
    # 3.创建窗口
    window = sg.Window('窗口标题', layout)

    # 4.事件循环
    while True:
        event, values = window.read()
        print(event, values)

        if event is None:  # 窗口关闭事件
            break

    # 5.关闭窗口
    window.close()


