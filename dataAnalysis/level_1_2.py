# -*- coding: utf-8 -*-
import pandas as pd

if __name__ == '__main__':
    # 创建行索引
    indexs = ['No1', 'No2', 'No3']
    # 创建字典
    dic = {
        '姓名': pd.Series(['娜娜', '淼淼', '依依'], index=indexs),
        '类型': pd.Series(['可爱单纯', '风骚火辣', '性感高冷'], index=indexs),
        '爱好': pd.Series(['逛街、电影、爱吃甜', '喝酒、蹦迪、爱吃辣', '看书、烘焙、爱吃酸'], index=indexs),
        '时间': pd.Series(['2019-2-14去看电影', '2019-2-16去蹦迪', '2019-2-18去烘焙'], index=indexs)
    }

    df = pd.DataFrame(dic)

    print(df)
