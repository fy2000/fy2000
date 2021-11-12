# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as abn

if __name__ == '__main__':
    # 第一小题 ============================================================
    data = pd.read_csv('/data/course_data/data_analysis/tips.csv')
    print(data.head())

    # 绘制没两列变量之间的关系用多变量关系分布图
    abn.pairplot(data)

    plt.show()

    # 第二小题 ===================================================================
    data = pd.read_csv('/data/course_data/data_analysis/tips.csv')
    # print(data.head())

    # 绘制没两列变量之间的关系用多变量关系分布图
    abn.pairplot(data, hue='sex')

    plt.show()

    # 第三小题 ====================================================================
    data = pd.read_csv('/data/course_data/data_analysis/tips.csv')
    # print(data.head())

    # 绘制没两列变量之间的关系用多变量关系分布图
    abn.pairplot(data, vars=['total_bill', 'tip'], kind='reg', diag_kind='kde')

    plt.show()