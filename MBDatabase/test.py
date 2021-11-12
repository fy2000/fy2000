# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    my_font = fm.FontProperties(fname='STSong.ttf')
    df = pd.read_excel("data/test.xlsx")

    df['月份'] = [((m.split('/')[1])+'月') for m in df['日期']]
    groups = df.groupby('月份').size()
    m_list = []
    dic = dict()
    for index, num in groups.items():
        dic[index] = num

    for i in range(1, 13):
        m_list.append(dic[str(i)+'月'])

    # for mm in range(0, 12):
    #     plt.bar(mm, m_list[mm])
    # plt.plot([str(i)+'月' for i in range(1, 13)], m_list, color='blue')

    # plt.xticks(range(0, 12), [str(i)+'月' for i in range(1, 13)], fontproperties=my_font)

    patches, l_text, p_text = plt.pie(m_list, labels=[str(i)+'月' for i in range(1, 13)], autopct='%.1f%%', shadow=False)
    for tet in l_text:
        tet.set_fontproperties(my_font)
    # plt.title('鼎科2020年月订单量', fontproperties=my_font)
    # plt.ylabel('订单数量', fontproperties=my_font)
    # plt.xlabel('月份', fontproperties=my_font)
    # plt.grid()
    plt.show()

    # print(df.head())
