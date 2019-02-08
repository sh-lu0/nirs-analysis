import numpy as np
import pandas as pd
import scipy as sp
from scipy import stats
import os
import csv
from matplotlib import pyplot as plt

# import seaborn as sns
# sns.set()

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
  rest = nirs_data['ch' + str(i+1) + '_rest']
  task = nirs_data['ch' + str(i+1) + '_task']
  print(rest)
  print(task)

  statictics, pvalue = stats.ttest_rel(task, rest)
  list = ['ch' + str(i+1), statictics, pvalue]
  writer.writerow(list)

f.close()
