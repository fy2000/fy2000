# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    my_font = fm.FontProperties(fname='/data/course_data/data_analysis/STSONG.TTF')

    df = pd.read_excel('/data/course_data/data_analysis/Commerce.xls')

    df.index = df['订单日期']
    # print(df.head())

    area18 = df['2018'].groupby('地区')['销售额'].sum()
    area17 = df['2017'].groupby('地区')['销售额'].sum()

    rate18 = (area18 - area17) / area17

    # 画图
    fig = plt.figure(figsize=(20,8),dpi=80)
    ax = fig.add_subplot(111)
    lin1 = ax.bar(area18.index, area18)
    ax.set_ylabel('2018销售额', fontproperties=my_font)
    ax.set_xlabel('地区', fontproperties=my_font)
    plt.xticks(range(0, len(area18.index)), area18.index, fontproperties=my_font)

    ax2 = ax.twinx()
    ax2.plot(rate18.index, rate18, color='red')
    ax2.set_ylabel('增长率', fontproperties=my_font)
    plt.show()


