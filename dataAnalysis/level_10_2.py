# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    my_font = fm.FontProperties(fname='/data/course_data/data_analysis/STSONG.TTF')

    df = pd.read_excel('/data/course_data/data_analysis/E-Business.xlsx')
    # print(df.head())
    city_group = df.groupby('地区').size()

    x = city_group.index.tolist()
    y = city_group.values.tolist()
    # print(y)

    # 画柱状图
    plt.subplot(3, 1, 1)
    rects = plt.bar(x, y)
    plt.xticks(x, fontproperties=my_font)

    count = 0
    for rect in rects:
        re_w = rect.get_x() + (rect.get_width() / 2)
        re_h = rect.get_height() + 1
        plt.text(re_w, re_h, str(y[count]), ha='center')
        count += 1

    plt.subplot(3, 1, 3)
    patches, l_text, p_text = plt.pie(y, labels=x, autopct='%.1f%%', shadow=False, radius=3)
    for t in l_text:
        t.set_fontproperties(my_font)

    plt.show()