import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import os
import csv
from matplotlib import pyplot as plt

# 表示桁数の指定
# %precision 3
# グラフをjupyter Notebook内に表示させるための指定
# %matplotlib inline

os.chdir('/Users/chiaki/Desktop/')
print("ファイル名を入力してください：")
filename = input()
nirs_data = pd.read_csv(filename + ".csv")

f = open('result_' + filename + '.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
label = ['ch', 'statictics', 'pvalue']
writer.writerow(label)

for i in range(68):
  nirs = nirs_data['ch' + str(i+1) + '_corr']
  # 標本平均
  mu = sp.mean(nirs)
  # 自由度
  df = 4
  # 標準誤差
  sigma = sp.std(nirs, ddof=1)
  se = sigma / sp.sqrt(5)
  # t値
  t_value = (mu - 0) / se

  statictics, pvalue = stats.ttest_1samp(nirs, 0)
  print(stats.ttest_1samp(nirs, 0))
  list = ['ch' + str(i+1), statictics, pvalue]
  writer.writerow(list)

f.close()
