import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

"""
静止画ヒートマップ用
"""
# データが格納されている作業ディレクトリまでパス指定
os.chdir("/Users/chiaki/Desktop/")
sns.set()

# スムージング済みのファイルを読み込み
print('ファイル名：')
filename = input()
df = pd.read_csv(filename+ '.csv', sep=',')

# マスク設定
mask = [[1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]]
mask = np.append(mask, [[1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                        [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]], axis=0)

fig = plt.figure()
frames = []

df_line = df['pvalue']
view_data = [[0, 0, 0, 0, df_line[0], 0, df_line[1], 0, df_line[2], 0, 0, 0, 0]]
view_data = np.append(view_data,
              [[0, 0, 0, df_line[3], 0, df_line[4], 0, df_line[5], 0, df_line[6], 0, 0, 0],
                [0, 0, 0, 0, df_line[7], 0, df_line[8], 0, df_line[9], 0, 0, 0, 0],
                [0, df_line[10], 0, df_line[11], 0, df_line[12], 0, df_line[13], 0, df_line[14], 0, df_line[15], 0],
                [df_line[16], 0, df_line[17], 0, df_line[18], 0, df_line[19], 0, df_line[20], 0, df_line[21], 0, df_line[22]],
                [0, df_line[23], 0, df_line[24], 0, df_line[25], 0, df_line[26], 0, df_line[27], 0, df_line[28], 0],
                [df_line[29], 0, df_line[30], 0, df_line[31], 0, df_line[32], 0, df_line[33], 0, df_line[34], 0,df_line[35]],
                [0, df_line[36], 0, df_line[37], 0, df_line[38], 0, df_line[39], 0, df_line[40], 0, df_line[41], 0],
                [df_line[42], 0, df_line[43], 0, df_line[44], 0, df_line[45], 0, df_line[46], 0, df_line[47], 0,df_line[48]],
                [0, df_line[49], 0, df_line[50], 0, df_line[51], 0, df_line[52], 0, df_line[53], 0, df_line[54], 0],
                [df_line[55], 0, df_line[56], 0, df_line[57], 0, df_line[58], 0, df_line[59], 0, df_line[60], 0,df_line[61]],
                [0, df_line[62], 0, df_line[63], 0, df_line[64], 0, df_line[65], 0, df_line[66], 0, df_line[67], 0]], axis=0)

sns.heatmap(view_data, annot=True, fmt='1.4f', linewidths=.5, center=0,
            yticklabels=False, xticklabels=False, mask=mask,cmap="bwr")  # 数値ありの時はannot=True
plt.show()
f = plt.plot()
frames.append([f])

input("Enter to close")
plt.close()

print("end")
