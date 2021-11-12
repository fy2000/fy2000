# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    my_font = fm.FontProperties(fname='/data/course_data/data_analysis/STSONG.TTF',size=10)
    df = pd.read_excel('/data/course_data/data_analysis/FIFA19.xlsx')
    ages = df['Age']
    num = int(max(ages) - min(ages) / 2)

    g_df = df.groupby('Position').size()

    # plt.hist(ages, bins=num)
    # plt.xticks(range(min(ages), max(ages))[::2])

    plt.pie(g_df, labels=g_df.index, autopct='%.1f%%', shadow=False, radius=2)

    plt.show()