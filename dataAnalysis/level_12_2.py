# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

if __name__ == '__main__':
    baby_df = pd.read_excel('/data/course_data/data_analysis/births.xlsx')
    # print(baby_df.head())

    # 先按性别分组
    sex_groups = baby_df.groupby('gender')
    F_group_df = sex_groups.get_group('F')
    M_group_df = sex_groups.get_group('M')
    # print(F_group.head())
    # print(M_group.head())

    F_year_group = F_group_df.groupby('year')
    M_year_group = M_group_df.groupby('year')

    Fx = []  # 男孩出生年份
    Fy = []  # 男孩出生数量
    Mx = []  # 女孩出生年份
    My = []  # 女孩出生数量
    for group_name, data_df in F_year_group:
        Fx.append(str(group_name))
        Fy.append(data_df['births'].sum())

    for group_name, data_df in F_year_group:
        Mx.append(str(group_name))
        My.append(data_df['births'].sum())

    plt.figure(figsize=(20, 8), dpi=80)

    with sbn.axes_style('white'):
        plt.subplot(211)
        rects = plt.bar(Fx, Fy)
        plt.xticks(range(0, len(Fx)), Fx)
        count = 0
        for rect in rects:
            xbar = rect.get_x() + rect.get_width() / 2
            ybar = rect.get_height() + 0.5
            plt.text(xbar, ybar, str(Fy[count]), ha='center')
            count += 1

    with sbn.axes_style('darkgrid'):
        plt.subplot(212)
        rects = plt.bar(Mx, My)
        plt.xticks(range(0, len(Mx)), Mx)
        count = 0
        for rect in rects:
            xbar = rect.get_x() + rect.get_width() / 2
            ybar = rect.get_height() + 0.5
            plt.text(xbar, ybar, str(My[count]), ha='center')
            count += 1

    plt.show()