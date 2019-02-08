#coding:utf-8

# from module.emg_processing import window_rms
from module.import_data import Import_data
from module.delete_data import Delete_data
import matplotlib.pyplot as plt
import os
import numpy as np
import pylab
import csv

"""
NIRSから取り出したTXTを入れると，
oxyデータと処理済みEMGのみのCSVが出力される
"""

print('データの格納場所を入力してください 例：/Users/username/Desktop/')
data_stored_area = str(input())
print('読み込むファイル名を入力してください')
file_name = input()
print('前頭葉のサンプル数(100くらい)')
front_sample = int(input())
print('後頭部のサンプル数(150~200くらい)')
back_sample = int(input())

# ---ファイル読み込み---
os.chdir(data_stored_area) # データが格納されている作業ディレクトリまでパス指定
import_data = Import_data(file_name) #インスタンス化
data = import_data.import_nirsdata()

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

    plt.plot(data['time'],data['ch' + str(i + 1) + '_oxy'])
    plt.title('ch' + str(i + 1) + '_oxy')

    pylab.axvspan(10, 30, facecolor="red", alpha=0.3)
    pylab.axvspan(50, 70, facecolor="red", alpha=0.3)
    pylab.axvspan(90, 110, facecolor="red", alpha=0.3)
    pylab.axvspan(130, 150, facecolor="red", alpha=0.3)
    pylab.axvspan(170, 190, facecolor="red", alpha=0.3)

    plt.xlabel("Oxy-Hb")
    plt.ylabel("Time[s]")
    plt.show()

for i in range(58):
    print(i+11)
    # root_data = data["ch" + str(i + 11) + "_oxy"]
    # plt.plot(data['time'],root_data, color='lightgray')

    window = np.ones(back_sample) / float(back_sample)
    y = np.convolve(data['ch' + str(i + 11) + '_oxy'], window, "same")
    data["ch" + str(i + 11) + "_oxy"] = y

    plt.plot(data['time'],data['ch' + str(i + 11) + '_oxy'])
    plt.title('ch' + str(i + 11) + '_oxy')

    pylab.axvspan(10, 30, facecolor="red", alpha=0.3)
    pylab.axvspan(50, 70, facecolor="red", alpha=0.3)
    pylab.axvspan(90, 110, facecolor="red", alpha=0.3)
    pylab.axvspan(130, 150, facecolor="red", alpha=0.3)
    pylab.axvspan(170, 190, facecolor="red", alpha=0.3)

    plt.xlabel("Oxy-Hb")
    plt.ylabel("Time[s]")
    plt.show()

# ---不要なデータ削除---
delete_data = Delete_data(data) #インスタンス化
data = delete_data.delete_nirsdata()

# ---書き出し---
data.to_csv("smoothing_" + file_name + ".csv")
print('OK')
