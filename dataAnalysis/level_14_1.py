# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    # 第一小题
    df = pd.read_csv('/data/course_data/data_analysis/BJ_tianqi.csv')

    # 观察发现每行的数据都没有缺失的情况 所以不用删除数据
    # 计算重复
    print(df.duplicated()[df.duplicated() == True])

    df["最高温度"] = df["最高温度"].str.replace("℃", "").astype('int')
    df["最低温度"] = df["最低温度"].str.replace("℃", "").astype('int')

    df['月份'] = [i[0:i.rindex('/')] for i in df['日期']]
    # print(df)
    m_groups = df.groupby('月份')

    for g_name, g_df in m_groups:
        max_temp = g_df['最高温度'].max()
        min_temp = g_df['最低温度'].min()
        difference = max_temp - min_temp
        plt.bar(g_name, difference)

    plt.xticks(range(0, len(m_groups.size().index)), m_groups.size().index, rotation=45)

    plt.show()

    # 第二小题
    # print(df.head())
    my_font = fm.FontProperties(fname='/data/course_data/data_analysis/STSONG.TTF', size=10)
    q_groups = df.groupby('空气质量').size()
    patches, ltexts, p_texts = plt.pie(q_groups, labels=q_groups.index, autopct='%.1f%%')

    for latext in ltexts:
        latext.set_fontproperties(my_font)

    plt.show()