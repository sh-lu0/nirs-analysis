#coding:utf-8
#!/usr/bin/env python

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy import signal


"""
相関係数

自己相関出してずらすバージョン
"""
# データが格納されている作業ディレクトリまでパス指定
os.chdir("/Users/chiaki/Desktop/")

print('読み込むファイル名を入力してください')
file_name = input()

result_f = pd.DataFrame(columns=[])
set_time = int(40)

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

time = df[:701]['time']

def make_square(off_time, on_time):
  off_time = np.zeros(87)
  on_time = np.ones(175)
  sq = np.hstack((off_time, on_time))
  sq = np.hstack((sq, off_time))
  return sq*0.05

def main():
  off_time = 87
  on_time = 175
  sq = make_square(off_time, on_time)
  center = off_time + on_time/2

  for i in range(68):
    corr_box = []
    plt.figure()
    for j in range(5):
      time_1 = int(j*701)
      time_2 = int(j * 701 + 701)

      nirs = df[time_1:time_2]['ch' + str(i + 1) + '_oxy']
      # print(nirs)

      # 自己相関出す
      acor = np.correlate(nirs, sq, "same")
      # print(acor)
      # 最大値のある行数
      acor_max = acor.argmax()
      # print(acor)
      # print(acor_max)


      # ずらす
      if acor_max < center:
        lag = center - acor_max
        print('max < center')
        off_after = lag - on_time / 2
        square_delay = make_square(off_after, on_time)
        # 長さ揃える
        square_delay = square_delay[int(center - acor_max):int(off_time * 2 + on_time)]
        nirs_cut = nirs[:int((off_time * 2 + on_time) -  (center - acor_max) + 1)]

      else:
        lag = acor_max - center
        off_after = off_time + lag - on_time / 2
        square_delay = make_square(off_after, on_time)
        # 長さ揃える
        nirs_cut = nirs[int(acor_max - center):int((acor_max - center) + off_time * 2 + on_time)]

      # print("nirs")
      # print(len(nirs_cut))
      # print("sq")
      # print(len(square_delay))

      # plt.plot(time[int(acor_max - center):int((acor_max - center) + off_time * 2 + on_time)], nirs_cut, "red")
      # plt.plot(time[int(acor_max - center):int((acor_max - center) + off_time * 2 + on_time)], square_delay,"blue")
      # plt.title('ch' + str(i + 1))
      # # plt.show()
      # plt.close()

      try:
        # 相関をとる
        corr = np.corrcoef(nirs_cut, square_delay)
        corr_box.append(corr[0, 1])
      except ValueError:
        print('Error')
        # plt.plot(nirs_cut, "red")
        # plt.plot(square_delay,"blue")
        # plt.title('ch' + str(i + 1))
        # plt.show()
        # plt.close()
        corr_box.append(0)

      print('ch' + str(i + 1) + '_corr')
    result_f['ch' + str(i + 1) + '_corr'] = corr_box
    result_f.to_csv("corr_" + file_name + ".csv")
  print('OK')


if __name__ == "__main__":
  main()
