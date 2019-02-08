#coding:utf-8
import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import csv

"""
筋電の大まかな動きをみる．
NIRSでとった筋電は2.5Vを基準としているため，平均値を0とする．
window_rms()で筋電を整流し，移動平均二乗平方根を使って処理する．
"""

def EMG_RMS(file_name):
    # データが格納されている作業ディレクトリまでパス指定
    os.chdir("/Users/chiaki/Desktop/")

    data = pd.read_csv(file_name + '.TXT', sep='\t')
    data.columns = ["time", "ch1", "ch2", "ch3"]
    time_array = data['time']

    # data = data - 2.5 #2.5Vを0にする
    data["ch1"] = data["ch1"] - (data["ch1"].sum(axis=0) / len(data["ch1"]))
    data["ch2"] = data["ch2"] - (data["ch2"].sum(axis=0) / len(data["ch2"]))
    data["ch3"] = data["ch3"] - (data["ch3"].sum(axis=0) / len(data["ch3"]))

    WINDOW_SIZE=101
    RMS_ch1 = window_rms(data["ch1"],WINDOW_SIZE)
    RMS_ch2 = window_rms(data["ch2"], WINDOW_SIZE)
    RMS_ch3 = window_rms(data["ch3"], WINDOW_SIZE)

    plt.plot(data["ch1"], color='lightgray')
    plt.plot(RMS_ch1)
    plt.xlabel("Time[ms]")
    plt.ylabel("EMG[V]")
    plt.show()

    plt.plot(data["ch2"], color='lightgray')
    plt.plot(RMS_ch2)
    plt.xlabel("Time[ms]")
    plt.ylabel("EMG[V]")
    plt.show()

    plt.plot(data["ch3"], color= 'lightgray')
    plt.plot(RMS_ch3)
    plt.xlabel("Time[ms]")
    plt.ylabel("EMG[V]")
    plt.show()

    # 書き出し
    df = pd.DataFrame({
        'time':time_array,
        'ch1':RMS_ch1,
        'ch2':RMS_ch2,
        'ch3':RMS_ch3})
    df.to_csv("processed_EMG" + file_name + ".csv")
    print('OK')

def window_rms(array, window_size):
    array_power = np.power(array, 2)
    window = np.ones(window_size) / float(window_size)
    return np.sqrt(np.convolve(array_power, window, "same"))