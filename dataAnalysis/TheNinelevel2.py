# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
import math
import random

if __name__ == '__main__':
    my_font = fm.FontProperties(fname='STSong.ttf')

    df = pd.read_csv('5Ggcdata.csv')
    pd.read_excel

    dsg = df.groupby('地市')
    num = dsg.size()
    a = range(10, 1000)
    b = range(100, 500)

    x = [random.choice(a) for i in range(0, 100)]
    y = [random.choice(b) for i in range(0, 100)]

    # 柱状图
    # plt.bar(x, y)

    # 直方图
    # plt.hist(x, 500)

    # 散点图
    # plt.scatter(x, y, alpha=0.5, c='red')

    # 饼图
    patches, l_text, p_text = plt.pie(num, labels=num.index, autopct='%.1f%%', shadow=False)
    for t in l_text:
        t.set_fontproperties(my_font)

    plt.show()
