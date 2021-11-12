# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm

if __name__ == '__main__':
    y1 = [1, 0, 1, 1, 2, 4, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 1, 1]
    y2 = [1, 0, 3, 1, 2, 2, 3, 4, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    x1 = [str(i) for i in range(11, 31)]

    # 导入中文字体
    my_font = fm.FontProperties(fname='STSong.ttf')

    # 方法一 同一块画布上画图
    # # 画图 我的
    # plt.plot(x1, y1, label='我')
    # # 画图 朋友的
    # plt.plot(x1, y2, label='朋友')
    # # 自定义X轴
    # plt.xticks(range(0, len(x1)), x1)
    # # 添加说明
    # plt.title('每个年龄段的交友数量统计', fontproperties=my_font)
    # plt.ylabel('交友数', fontproperties=my_font)
    # plt.xlabel('年龄', fontproperties=my_font)
    # plt.legend(prop=my_font)
    # # 显示图像
    # plt.show()

    # 方法二 分不同的画布画图
    # 画图 我的
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, label='我')
    # 自定义X轴
    plt.xticks(range(0, len(x1)), x1)
    # 添加说明
    plt.title('每个年龄段的交友数量统计', fontproperties=my_font)
    plt.ylabel('交友数', fontproperties=my_font)
    plt.xlabel('年龄', fontproperties=my_font)
    plt.legend(prop=my_font)

    # 画图 朋友的
    plt.subplot(2, 1, 2)
    plt.plot(x1, y2, label='朋友', color='red')
    # 自定义X轴
    plt.xticks(range(0, len(x1)), x1)
    # 添加说明
    plt.title('每个年龄段的交友数量统计', fontproperties=my_font)
    plt.ylabel('交友数', fontproperties=my_font)
    plt.xlabel('年龄', fontproperties=my_font)
    plt.legend(prop=my_font)

    # 调整子图间距
    plt.tight_layout()
    plt.subplots_adjust()

    # 显示图像
    plt.show()
