# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

if __name__ == '__main__':
    baby_df = pd.read_excel('/data/course_data/data_analysis/births.xlsx')
    # print(baby_df.head())

    year_groups = baby_df.groupby('year')

    x = []
    y = []
    for group_name, data_df in year_groups:
        x.append(group_name)
        y.append(data_df['births'].sum())

    plt.figure(figsize=(20, 8), dpi=80)
    sbn.set()
    rects = plt.bar(x, y)

    count = 0
    for rect in rects:
        xbar = rect.get_x() + rect.get_width() / 2
        ybar = rect.get_height() + 0.5
        plt.text(xbar, ybar, str(y[count]), ha='center')
        count += 1

    plt.show()