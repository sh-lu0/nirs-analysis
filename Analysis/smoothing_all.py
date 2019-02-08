#coding:utf-8

# from module.emg_processing import window_rms
from module.import_data import Import_data
from module.delete_data import Delete_data
import matplotlib.pyplot as plt
import os
import numpy as np
import pylab
import csv
import pandas as pd

"""
NIRSから取り出したTXTを入れると，
oxyデータと処理済みEMGのみのCSVが出力される
"""

# print('データの格納場所を入力してください 例：/Users/username/Desktop/')
# data_stored_area = str(input())
print('読み込むファイル名を入力してください')
file_name = input()
print('前頭葉のサンプル数(100くらい)')
front_sample = int(input())
print('後頭部のサンプル数(150~200くらい)')
back_sample = int(input())

# ---ファイル読み込み---
os.chdir('/Users/chiaki/Desktop/')
# os.chdir(data_stored_area) # データが格納されている作業ディレクトリまでパス指定
# import_data = Import_data(file_name) #インスタンス化
# data = import_data.import_nirsdata()
data = pd.read_csv(file_name + '.csv', sep=',')
print('import_nirs_data')
data.columns = ['index','time','ch1_oxy', 'ch1_deoxy',
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


# ---EMG処理---
# data["EMG_ch1"] = data["EMG_ch1"] - (data["EMG_ch1"].sum(axis=0) / len(data["EMG_ch1"]))
# data["EMG_ch2"] = data["EMG_ch2"] - (data["EMG_ch2"].sum(axis=0) / len(data["EMG_ch2"]))
# data["EMG_ch3"] = data["EMG_ch3"] - (data["EMG_ch3"].sum(axis=0) / len(data["EMG_ch3"]))
#
# WINDOW_SIZE = 101
# RMS_ch1 = window_rms(data["EMG_ch1"], WINDOW_SIZE)
# RMS_ch2 = window_rms(data["EMG_ch2"], WINDOW_SIZE)
# RMS_ch3 = window_rms(data["EMG_ch3"], WINDOW_SIZE)

# plt.plot(data["EMG_ch1"], color='lightgray')
# plt.plot(RMS_ch1)
# plt.xlabel("Time[ms]")
# plt.ylabel("EMG[V]")
# plt.show()
#
# plt.plot(data["EMG_ch2"], color='lightgray')
# plt.plot(RMS_ch2)
# plt.xlabel("Time[ms]")
# plt.ylabel("EMG[V]")
# plt.show()
#
# plt.plot(data["EMG_ch3"], color='lightgray')
# plt.plot(RMS_ch3)
# plt.xlabel("Time[ms]")
# plt.ylabel("EMG[V]")
# plt.show()
#
# data["EMG_ch1"] = RMS_ch1
# data["EMG_ch2"] = RMS_ch2
# data["EMG_ch3"] = RMS_ch3

# ---NIRS処理---
for i in range(10):
    print(i+1)
    # root_data = data["ch" + str(i + 1) + "_oxy"]
    # plt.plot(data['time'],root_data, color='lightgray')

    window = np.ones(front_sample) / float(front_sample) # 移動平均をとるための配列を設定
    y = np.convolve(data['ch' + str(i + 1) + '_oxy'], window, "same") # 配列の長さがmax(M,N)となり、長い方の配列に要素数を合わせる
    data["ch" + str(i + 1) + "_oxy"] = y

    y_deoxy = np.convolve(data['ch' + str(i + 1) + '_deoxy'], window, "same")
    data["ch" + str(i + 1) + "_deoxy"] = y_deoxy

    plt.plot(data['time'],data['ch' + str(i + 1) + '_oxy'],"red")
    plt.plot(data['time'],data['ch' + str(i + 1) + '_deoxy'],"blue")
    plt.title('ch' + str(i + 1))

    pylab.axvspan(10, 30, facecolor="red", alpha=0.3)
    pylab.axvspan(50, 70, facecolor="red", alpha=0.3)
    pylab.axvspan(90, 110, facecolor="red", alpha=0.3)
    pylab.axvspan(130, 150, facecolor="red", alpha=0.3)
    pylab.axvspan(170, 190, facecolor="red", alpha=0.3)

    plt.xlabel("Oxy-Hb")
    plt.ylabel("Time[s]")
    plt.savefig("/Users/chiaki/Desktop/smoothing_image/smoothing" + str(i+1) + ".png")
    # plt.show()
    plt.close()

for i in range(58):
    print(i+11)
    # root_data = data["ch" + str(i + 11) + "_oxy"]
    # plt.plot(data['time'],root_data, color='lightgray')

    window = np.ones(back_sample) / float(back_sample)
    y = np.convolve(data['ch' + str(i + 11) + '_oxy'], window, "same")
    data["ch" + str(i + 11) + "_oxy"] = y

    y_deoxy = np.convolve(data['ch' + str(i + 11) + '_deoxy'], window, "same")
    data["ch" + str(i + 11) + "_deoxy"] = y_deoxy

    plt.plot(data['time'],data['ch' + str(i + 11) + '_oxy'],"red")
    plt.plot(data['time'],data['ch' + str(i + 11) + '_deoxy'],"blue")
    plt.title('ch' + str(i + 11))

    pylab.axvspan(10, 30, facecolor="red", alpha=0.3)
    pylab.axvspan(50, 70, facecolor="red", alpha=0.3)
    pylab.axvspan(90, 110, facecolor="red", alpha=0.3)
    pylab.axvspan(130, 150, facecolor="red", alpha=0.3)
    pylab.axvspan(170, 190, facecolor="red", alpha=0.3)

    plt.xlabel("Hb")
    plt.ylabel("Time[s]")
    plt.savefig("/Users/chiaki/Desktop/smoothing_image/smoothing" + str(i+11) + ".png")
    plt.close()
    # plt.show()

# ---不要なデータ削除---
delete_data = Delete_data(data) #インスタンス化
data = delete_data.delete_nirsdata()

# ---書き出し---
data.to_csv("smoothing_" + file_name + ".csv")
print('OK')
