# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import os
from module.import_data import Import_data
from module.delete_data import Delete_data
import pandas as pd

def main():
    # print('データの格納場所を入力してください 例：/Users/username/Desktop/')
    # data_stored_area = str(input())
    print('読み込むファイル名を入力してください')
    file_name = input()
    print('REST_TIME:')
    rest_time = int(input())
    print('TASK_TIME:')
    task_time = int(input())

    set_time=rest_time*2+task_time

    # ファイル読み込み
    os.chdir('/Users/chiaki/Desktop/')
    # os.chdir(data_stored_area) # データが格納されている作業ディレクトリまでパス指定
    import_data = Import_data(file_name) # インスタンス化
    df = import_data.import_nirsdata()

    # トレンド除去
    # result_f = pd.DataFrame(columns=[])
    result_f = pd.DataFrame()
    result_f['time'] = []
    for j in range(68):
        result_box = []
        result_box_deoxy = []
        time_box = []
        for i in range(5):
            time_0 = int((set_time*i)/0.057)
            time_1 = int((set_time*i+rest_time)/0.057)
            time_2 = int((set_time*i+rest_time+task_time)/0.057)
            time_3 = int((set_time*i+rest_time*2+task_time)/0.057)

            if (i == 0):
                X = df[:time_1]['time']
                X = pd.concat([X,df[time_2:time_3]['time']])

                Y = df[:time_1]['ch'+ str(j+1) + '_oxy']
                Y = pd.concat([Y,df[time_2:time_3]['ch'+ str(j+1) + '_oxy']])

                Y_deoxy = df[:time_1]['ch'+ str(j+1) + '_deoxy']
                Y_deoxy = pd.concat([Y_deoxy,df[time_2:time_3]['ch'+ str(j+1) + '_deoxy']])

                A = np.array([X,np.ones(len(X))])
                A = A.T
                a,b = np.linalg.lstsq(A,Y)[0]
                a_deoxy, b_deoxy = np.linalg.lstsq(A, Y_deoxy)[0]

                time = df[:time_3]['time']
                result = df[:time_3]['ch'+ str(j+1) + '_oxy'] - (a * time + b)
                result_deoxy = df[:time_3]['ch'+ str(j+1) + '_deoxy'] - (a_deoxy * time + b_deoxy)

                result_box.extend(result)
                result_box_deoxy.extend(result_deoxy)
                time_box.extend(time)

                # plt.plot(X, Y, "ro")
                # plt.plot(time,df[:time_3]['ch'+ str(j+1) + '_oxy'],"lightgray")
                # plt.plot(X,(a*X+b),"g--")
                # plt.plot(time, result,"blue")
                # plt.grid()
                # plt.show()

            else:
                X = df[time_0:time_1]['time']
                X = pd.concat([X, df[time_2:time_3]['time']])

                Y = df[time_0:time_1]['ch'+ str(j+1) + '_oxy']
                Y = pd.concat([Y, df[time_2:time_3]['ch'+ str(j+1) + '_oxy']])

                Y_deoxy = df[time_0:time_1]['ch'+ str(j+1) + '_deoxy']
                Y_deoxy = pd.concat([Y_deoxy,df[time_2:time_3]['ch'+ str(j+1) + '_deoxy']])

                A = np.array([X, np.ones(len(X))])
                A = A.T
                a, b = np.linalg.lstsq(A, Y)[0]
                a_deoxy, b_deoxy = np.linalg.lstsq(A, Y_deoxy)[0]

                time = df[time_0:time_3]['time']
                result = df[time_0:time_3]['ch'+ str(j+1) + '_oxy'] - (a * time + b)
                result_deoxy = df[time_0:time_3]['ch'+ str(j+1) + '_deoxy'] - (a_deoxy * time + b_deoxy)

                result_box.extend(result)
                result_box_deoxy.extend(result_deoxy)
                time_box.extend(time)

                # plt.plot(X,Y,"ro")
                # plt.plot(time,df[time_0:time_3]['ch'+ str(j+1) + '_oxy'],"lightgray")
                # plt.plot(X,(a*X+b),"g--")
                # plt.plot(time, result,"blue")
                # plt.grid()
                # plt.show()

        result_f['time'] = time_box
        result_f['ch'+ str(j+1) + '_oxy'] = result_box
        result_f['ch'+ str(j+1) + '_deoxy'] = result_box_deoxy
        plt.plot(df['ch'+ str(j+1) + '_oxy'],"lightgray")
        plt.plot(result_f['ch'+ str(j+1) + '_oxy'], "red")
        plt.plot(result_f['ch'+ str(j+1) + '_deoxy'], "blue")
        plt.grid()
        plt.savefig("/Users/chiaki/Desktop/detrend_image/detrend" + str(j+1) + ".png")
        # plt.show()
        plt.close()

    # 書き出し
    result_f.to_csv("detrend_" + file_name + ".csv")
    print('OK')

if __name__ == '__main__':
    main()
