# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

if __name__ == '__main__':
    # 第一小题
    data = pd.read_csv('/data/course_data/data_analysis/tips.csv')

    print(data.head())

    sbn.distplot(data['size'], kde=True)
    plt.show()

    # 第二小题
    data = pd.read_csv('/data/course_data/data_analysis/tips.csv')

    # print(data.head())
    # 使用切片获取多个列
    usedata = data[['size', 'tip']]
    sbn.jointplot(x='size', y='tip', data=usedata, kind='reg')
    plt.show()