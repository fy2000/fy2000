# -*- coding: utf-8 -*-
from matplotlib import font_manager
from matplotlib import pyplot as plt
import math
import numpy as np

if __name__ == '__main__':
    # 加载字体
    my_font = font_manager.FontProperties(fname='STSong.ttf')

    # 构造正弦三角函数的曲线
    x = np.linspace(-np.pi, np.pi, 50)
    y = np.sin(x)

    ax = plt.gca()
    # 不显示边框
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')

    # 移动坐标原点到（0,0）点
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    # 画曲线
    ax.plot(x, y, color='red', label='正弦曲线')

    # 画图例
    ax.legend(prop=my_font)

    # 不显示坐标轴
    plt.xticks([])
    plt.yticks([])

    # 显示图像
    plt.show()
