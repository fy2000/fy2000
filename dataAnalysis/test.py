# -*- coding: utf-8 -*-
import pandas as pd
from matplotlib import font_manager
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sbn


if __name__ == '__main__':
    my_font = font_manager.FontProperties(fname='STSong.ttf', size=12)
    x = np. linspace(-np.pi, np.pi, 250)
    y = np.sin(x)
    z = np.cos(x)

    plt.plot(x, y, label='正弦')
    plt.plot(x, z, label='余弦')

    plt.title('正余弦图像', fontproperties=my_font)
    plt.legend(prop=my_font)
    plt.grid()
    plt.show()
