import csv
import pandas as pd
df = pd.read_excel("Column Forces.xlsx",sheet_name='Sheet2')
df.info()
df['maxValue']=0 #增加空值列
rows = len(df.axes[0])  # 得到总行数
for i in range(4,rows,8):
    row_first_max = df.iloc[i][-3:-1].max()  # 取每行最后4列。从[P	V	M	T]，然后得到最大值
    row_second_max = df.iloc[i+1][-3:-1].max() 
    row_third_max= df.iloc[i+2][-3:-1].max() 
    row_fourth_max= df.iloc[i+3][-3:-1].max() 
    maxi= max ([row_first_max,row_second_max,row_third_max,row_fourth_max])
    df.loc[i, 'maxValue'] = maxi
df.to_excel('Column Forces pandas_method1.xlsx', sheet_name='Sheet1', index=False)
