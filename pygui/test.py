# -*- coding: utf-8 -*-
# 1.导入GUI库
import PySimpleGUI as Sg

# 2.定义布局，定义行数
layout = [
    [Sg.Text('请输入基本信息')],
    [Sg.Text('姓名'), Sg.InputText('张 明明')],
    [Sg.Text('性别'), Sg.InputText('男', key='-sex-')],
    [Sg.Text('国籍'), Sg.InputText('中国')],
    [Sg.Button('确认'), Sg.Button('取消')]
]

if __name__ == '__main__':
    # 3.创建窗口
    window = Sg.Window('Window Title', layout)

    # 4.事件循环
    while True:
        event, values = window.read()

        if event is Sg.WIN_CLOSED:  # 窗口关闭事件
            break
        if event == '确认':
            print(values)
        if event == '取消':
            print(values['-sex-'])

    # 5.关闭窗口
    window.close()




