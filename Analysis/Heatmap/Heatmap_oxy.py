#!/usr/bin/env python3
# -*- coding: utf8 -*-
import tkinter as tk
import csv
import time
import threading
from pytz import timezone
from dateutil import parser
import pandas as pd
import numpy as np
import os

"""
fNIRSで計測した68chをアニメーションで表示する
前方10ch，後方58ch
前方左前から1chで始まる場合
"""

"""
やることリスト
・時刻表示
・戻る/進む/リセットのところ修正
・故障chの色変える
"""

########################################################
# データ読み込み
########################################################

print('データの格納場所を入力してください 例：/Users/username/Desktop/')
data_stored_area = str(input())
# データが格納されている作業ディレクトリまでパス指定
os.chdir(data_stored_area)

print('読み込むファイル名を入力してください')
file_name = input()
df = pd.read_csv(file_name + ".csv")

pixel_frame = []

# TODO: 時刻表示
time_frame = df['time']

line_count = 0
for _ in range(len(df.index)):
    # TODO:まとめようね
    df_line = df.loc[line_count]
    # print(df_line)
    pixels = [[0 for i in range(13)] for j in range(12)]

    pixels_row = 0;
    pixels_column = 0;
    df_line_num = 0;

    # 前
    pixels[0][4] = df_line[3]
    pixels[0][6] = df_line[5]
    pixels[0][8] = df_line[7]
    pixels[1][3] = df_line[9]
    pixels[1][5] = df_line[11]
    pixels[1][7] = df_line[13]
    pixels[1][9] = df_line[15]
    pixels[2][4] = df_line[17]
    pixels[2][6] = df_line[19]
    pixels[2][8] = df_line[21]

    # 後ろ
    pixels[3][1] = df_line[23]
    pixels[3][3] = df_line[25]
    pixels[3][5] = df_line[27]
    pixels[3][7] = df_line[29]
    pixels[3][9] = df_line[31]
    pixels[3][11] = df_line[33]
    pixels[4][0] = df_line[35]
    pixels[4][2] = df_line[37]
    pixels[4][4] = df_line[39]
    pixels[4][6] = df_line[41]
    pixels[4][8] = df_line[43]
    pixels[4][10] = df_line[45]
    pixels[4][12] = df_line[47]
    pixels[5][1] = df_line[49]
    pixels[5][3] = df_line[51]
    pixels[5][5] = df_line[53]
    pixels[5][7] = df_line[55]
    pixels[5][9] = df_line[57]
    pixels[5][11] = df_line[59]
    pixels[6][0] = df_line[61]
    pixels[6][2] = df_line[63]
    pixels[6][4] = df_line[65]
    pixels[6][6] = df_line[67]
    pixels[6][8] = df_line[69]
    pixels[6][10] = df_line[71]
    pixels[6][12] = df_line[73]
    pixels[7][1] = df_line[75]
    pixels[7][3] = df_line[77]
    pixels[7][5] = df_line[79]
    pixels[7][7] = df_line[81]
    pixels[7][9] = df_line[83]
    pixels[7][11] = df_line[85]
    pixels[8][0] = df_line[87]
    pixels[8][2] = df_line[89]
    pixels[8][4] = df_line[91]
    pixels[8][6] = df_line[93]
    pixels[8][8] = df_line[95]
    pixels[8][10] = df_line[97]
    pixels[8][12] = df_line[99]
    pixels[9][1] = df_line[101]
    pixels[9][3] = df_line[103]
    pixels[9][5] = df_line[105]
    pixels[9][7] = df_line[107]
    pixels[9][9] = df_line[109]
    pixels[9][11] = df_line[111]
    pixels[10][0] = df_line[113]
    pixels[10][2] = df_line[115]
    pixels[10][4] = df_line[117]
    pixels[10][6] = df_line[119]
    pixels[10][8] = df_line[121]
    pixels[10][10] = df_line[123]
    pixels[10][12] = df_line[125]
    pixels[11][1] = df_line[127]
    pixels[11][3] = df_line[129]
    pixels[11][5] = df_line[131]
    pixels[11][7] = df_line[133]
    pixels[11][9] = df_line[135]
    pixels[11][11] = df_line[137]
    pixel_frame.append(pixels)
    line_count += 1

########################################################
# GUI作成
########################################################

frame_index = 0
animation_on = False
# TEMPERATURE_MAX = 0.5
# TEMPERATURE_MIN = -0.5
print('RANGE(20で0.2が最大値):')
TEMPERATURE_RANGE = int(input())

root = tk.Tk()
root.title("fNIRS_HEATMAP")
root.geometry("365x420")

# 時刻テキスト定義
lb_time = tk.Label(text='Time')

# グリッド定義
color_grids = []
for i in range(0, 12):
    color_grid_row = []
    for j in range(0, 13):
        color_grid_row.append(tk.Label(text='     ', bg='#f0f0f0'))
    color_grids.append(color_grid_row)


# アニメーション定義
class AnimationThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global frame_index
        global animation_on
        global speed_var

        while animation_on:
            frame = pixel_frame[frame_index]
            for i in range(0, 12):
                for j in range(0, 13):
                    temp = frame[i][j]
                    if temp*100 > TEMPERATURE_RANGE:
                        color_grids[i][j].configure(bg="#ff0000") #プラス範囲以外
                    elif temp*100 < -TEMPERATURE_RANGE:
                        color_grids[i][j].configure(bg="#0000ff")  # マイナス範囲以外
                    elif temp == 0:
                        color_grids[i][j].configure(bg="#f0f0f0") # チャンネル以外をマスク
                    elif temp > 0:
                        temp = temp*100
                        r = 255
                        g = 255 - int(255 / TEMPERATURE_RANGE *temp)
                        b = 255 - int(255 / TEMPERATURE_RANGE *temp)
                        color = '#%02x%02x%02x' % (r, g, b)
                        color_grids[i][j].configure(bg=color)
                    elif temp < 0:
                        temp = temp * 100
                        r = 255 - int(255 / TEMPERATURE_RANGE * abs(temp))
                        g = 255 - int(255 / TEMPERATURE_RANGE * abs(temp))
                        b = 255
                        color = '#%02x%02x%02x' % (r, g, b)
                        color_grids[i][j].configure(bg=color)
                    else:
                        color_grids[i][j].configure(bg="#000000") # エラー
            lb_time.configure(text='{:.3f}'.format(time_frame[frame_index]))
            frame_index += 1
            time.sleep(float(speed_var.get()[:-2]))  # 単位を削除して変換


# アニメーション開始/停止イベントハンドラ
def animation():
    global animation_on
    animation_on = not animation_on
    if animation_on:
        # アニメーションスレッド生成・開始
        th_anim = AnimationThread()
        th_anim.start()
        bt_anim.configure(text="Stop")
    else:
        bt_anim.configure(text="Start")


# ステップ実行関数
def update_grids(step):
    global frame_index
    frame_index += step
    if frame_index < 0:
        frame_index = 0
    frame = pixel_frame[frame_index]
    for i in range(0, 12):
        for j in range(0, 13):
            temp = frame[i][j]
            temp_diff = 0
            if temp == 0:
                color_grids[i][j].configure(bg="#fff")
            else:
                if temp < TEMPERATURE_MIN:
                    temp_diff = 0
                elif temp > TEMPERATURE_MAX:
                    temp_diff = TEMPERATURE_RANGE
                else:
                    temp_diff = temp - TEMPERATURE_MIN
                r = 255
                g = 255 - int(temp_diff / TEMPERATURE_RANGE * 255)
                b = 255 - int(temp_diff / TEMPERATURE_RANGE * 255)
                color = '#%02x%02x%02x' % (r, g, b)
                color_grids[i][j].configure(bg=color)
                # lb_time.configure(text=time_frame[frame_index])

# ステップ実行（戻る）ハンドラ
def step_back():
    update_grids(-1)

# ステップ実行（進む）ハンドラ
def step_next():
    update_grids(1)

# リセットハンドラ
def reset():
    global frame_index
    frame_index = -1
    update_grids(1)

# アニメーション開始/停止ボタン定義
bt_anim = tk.Button(root, width=6, height=2, text="Start", command=animation)

# ステップ実行（戻る）ボタン定義
bt_back = tk.Button(root, width=6, height=2, text="Back", command=step_back)

# ステップ実行（進む）ボタン定義
bt_next = tk.Button(root, width=6, height=2, text="Next", command=step_next)

# リセットボタン定義
bt_reset = tk.Button(root, width=6, height=2, text="Reset", command=reset)

# ドロップダウンリスト（オプションメニュー）定義
speed_vars = ["0.057 s", "0.1 s", "0.2 s", "0.3 s", "0.4 s", "0.5 s", "0.6 s", "0.7 s", "0.8 s", "0.9 s", "1.0 s"]
speed_var = tk.StringVar()
speed_var.set(speed_vars[0])  # デフォルト値
dl_speed = tk.OptionMenu(root, speed_var, *speed_vars)

########################################################

# ボタン配置
bt_anim.grid(row=0, rowspan=1, column=0, columnspan=4, padx=0, pady=0)
# 再生スピード設定配置
dl_speed.grid(row=0, rowspan=1, column=4, columnspan=4, padx=0, pady=0)
# lb_speed.grid(row=0, rowspan=1, column=7, columnspan=1, padx=0, pady=0)

# ボタン配置
bt_back.grid(row=1, rowspan=1, column=0, columnspan=4, padx=0, pady=0)
bt_next.grid(row=1, rowspan=1, column=4, columnspan=4, padx=0, pady=0)

# 時刻情報配置
lb_time.grid(row=2, rowspan=1, column=0, columnspan=8, padx=0, pady=0)

# グリッド配置
for i in range(0, 12):
    for j in range(0, 13):
        color_grids[i][j].grid(row=(i + 3), rowspan=1, column=j, columnspan=1, padx=1, pady=1)

# ボタン配置
bt_reset.grid(row=1, rowspan=1, column=8, columnspan=4, padx=0, pady=0)


########################################################

# ウィンドウを閉じるときにアニメーションのスレッドが動いていたら、先にそちらを止めてから終了させる
def window_close():
    global animation_on
    if animation_on:
        animation_on = False
    root.destroy()


root.protocol("WM_DELETE_WINDOW", window_close)

# メインループ開始
root.mainloop()
