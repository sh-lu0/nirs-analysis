#coding:utf-8
import os
import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import sys

sys.path.append('/Users/chiaki/Library/Python/3.7/lib/python/site-packages')

import nipy.modalities.fmri.hrf as hrf

"""
t:配列
HRFをサンプリングする時間のベクトル

peak_delay：float、オプション
ピークの遅れ
6

under_delay：float、オプション
アンダーシュートの遅延
16

peak_disp：float、オプション
ピークの幅（分散）
1

under_disp：float、オプション
アンダーシュートの幅（分散）
1

p_u_ratio：float、オプション
アンダーシュート比に対するピーク。ピークから引く前にアンダーシュートをこの値で割った値
6

normalize：{True、False}、オプション
Trueの場合、戻る前にHRF値をそれらの合計で割ります。SPMはこれをデフォルトで行います
True
"""

"""
相関係数
"""
# t = np.arange(0, 526, 1)
# ff = hrf.spm_hrf_compat(t, peak_delay=298, under_delay=100, peak_disp=193, under_disp=17, p_u_ratio=6, normalize=True)
# plt.plot(ff, "blue")
# plt.savefig('corr.png')


# データが格納されている作業ディレクトリまでパス指定
os.chdir("/Users/chiaki/Desktop/")

print('読み込むファイル名を入力してください')
file_name = input()

result_f = pd.DataFrame(columns=[])

# ---ファイル読み込み---
df = pd.read_csv(file_name + '.csv', sep=',')
df.columns = ['index', 'index2','time','ch1_oxy', 'ch1_deoxy',
                'ch2_oxy', 'ch2_deoxy', 'ch3_oxy', 'ch3_deoxy',
                'ch4_oxy', 'ch4_deoxy', 'ch5_oxy', 'ch5_deoxy',
                'ch6_oxy', 'ch6_deoxy', 'ch7_oxy', 'ch7_deoxy',
                'ch8_oxy', 'ch8_deoxy', 'ch9_oxy', 'ch9_deoxy',
                'ch10_oxy', 'ch10_deoxy', 'ch11_oxy', 'ch11_deoxy',
                'ch12_oxy', 'ch12_deoxy', 'ch13_oxy', 'ch13_deoxy',
                'ch14_oxy', 'ch14_deoxy',  'ch15_oxy', 'ch15_deoxy',
                'ch16_oxy', 'ch16_deoxy',  'ch17_oxy', 'ch17_deoxy',
                'ch18_oxy', 'ch18_deoxy',  'ch19_oxy', 'ch19_deoxy',
                'ch20_oxy', 'ch20_deoxy',  'ch21_oxy', 'ch21_deoxy',
                'ch22_oxy', 'ch22_deoxy',  'ch23_oxy', 'ch23_deoxy',
                'ch24_oxy', 'ch24_deoxy',  'ch25_oxy', 'ch25_deoxy',
                'ch26_oxy', 'ch26_deoxy',  'ch27_oxy', 'ch27_deoxy',
                'ch28_oxy', 'ch28_deoxy',  'ch29_oxy', 'ch29_deoxy',
                'ch30_oxy', 'ch30_deoxy',  'ch31_oxy', 'ch31_deoxy',
                'ch32_oxy', 'ch32_deoxy',  'ch33_oxy', 'ch33_deoxy',
                'ch34_oxy', 'ch34_deoxy',  'ch35_oxy', 'ch35_deoxy',
                'ch36_oxy', 'ch36_deoxy',  'ch37_oxy', 'ch37_deoxy',
                'ch38_oxy', 'ch38_deoxy',  'ch39_oxy', 'ch39_deoxy',
                'ch40_oxy', 'ch40_deoxy',  'ch41_oxy', 'ch41_deoxy',
                'ch42_oxy', 'ch42_deoxy',  'ch43_oxy', 'ch43_deoxy',
                'ch44_oxy', 'ch44_deoxy',  'ch45_oxy', 'ch45_deoxy',
                'ch46_oxy', 'ch46_deoxy',  'ch47_oxy', 'ch47_deoxy',
                'ch48_oxy', 'ch48_deoxy',  'ch49_oxy', 'ch49_deoxy',
                'ch50_oxy', 'ch50_deoxy',  'ch51_oxy', 'ch51_deoxy',
                'ch52_oxy', 'ch52_deoxy',  'ch53_oxy', 'ch53_deoxy',
                'ch54_oxy', 'ch54_deoxy',  'ch55_oxy', 'ch55_deoxy',
                'ch56_oxy', 'ch56_deoxy',  'ch57_oxy', 'ch57_deoxy',
                'ch58_oxy', 'ch58_deoxy',  'ch59_oxy', 'ch59_deoxy',
                'ch60_oxy', 'ch60_deoxy', 'ch61_oxy', 'ch61_deoxy',
                'ch62_oxy', 'ch62_deoxy', 'ch63_oxy', 'ch63_deoxy',
                'ch64_oxy', 'ch64_deoxy', 'ch65_oxy', 'ch65_deoxy',
                'ch66_oxy', 'ch66_deoxy', 'ch67_oxy', 'ch67_deoxy',
                'ch68_oxy', 'ch68_deoxy',
                ]

def main():
  t = np.arange(0, 526, 1)
  ff = hrf.spm_hrf_compat(t, peak_delay=298, under_delay=386, peak_disp=17, under_disp=17, p_u_ratio=6, normalize=True)
  print(len(ff))

  for i in range(68):
    corr_box = []
    for j in range(5):
      time_1 = int(j*701)
      time_2 = int(j*701 + 526)
      nirs = df[time_1:time_2]['ch' + str(i + 1) + '_oxy']
      # print(len(nirs))
      # print(len(square))

      # 相関
      corr = np.corrcoef(ff, nirs)
      corr_box.append(corr[0, 1])

      plt.plot(ff, "blue")
      plt.savefig('corr.png')

      # plt.plot(nirs, "red")
      # plt.plot(df[time_1:time_2]['time'], square, "blue")

      # print(len(ff))
      # plt.plot(ff, "blue")

      # plt.savefig('corr.png')

    result_f['ch' + str(i + 1) + '_corr'] = corr_box
    result_f.to_csv("hrf_corr_" + file_name + ".csv")
  print('OK')


if __name__ == "__main__":
  main()
