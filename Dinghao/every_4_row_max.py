import csv
import pandas as pd
df = pd.read_excel("Column Forces.xlsx",sheet_name='Sheet2')
df.info()
df['maxValue']=0 #增加空值列
# print( df.head(10) )
rows = len(df.axes[0])  # 得到总行数
# print(rows)
# print("_______________________________0 begin ________________________________")
# print(df.iloc[0])
# print("_______________________________0 end ________________________________")
for i in range(4,rows,8):
    # print("i = ")
    # print(i)
    row_first = df.iloc[i][-6:]  # 取每行最后6列。从[STORY	工况	P	V	M	T]
    row_second = df.iloc[i+1][-6:]
    row_third= df.iloc[i+2][-6:]
    row_fourth= df.iloc[i+3][-6:]
    # print(type(row_first))
    # print("_______________________________  row_first =  ________________________________")
    # print(row_first)
    # print("_______________________________  row_first[-1] =  ________________________________")
    # print(row_first[-1])
    # print("_______________________________  row_first[-2] =  ________________________________")
    # print(row_first[-2])
    # print("row_first[-3:] = ")
    # print(row_first[-3:])
    # print("------------row_first[-3:-1].max() -----------------")
    row_first_max = row_first[-3:-1].max()
    # print(row_first_max )  #取第一行 [P	V	M	T]的最大值
    # print("------------row_second[-3:-1].max() -----------------")
    row_second_max = row_second[-3:-1].max()
    # print(row_second_max)  #取 [P	V	M	T]的最大值
    # print("------------row_third[-3:-1].max() -----------------")
    row_third_max = row_third[-3:-1].max()
    # print(row_third_max)  #取 [P	V	M	T]的最大值
    # print("------------row_fourth[-3:-1].max() -----------------")
    row_fourth_max = row_fourth[-3:-1].max()
    # print(row_fourth_max )  #取 [P	V	M	T]的最大值
    maxi= max ([row_first_max,row_second_max,row_third_max,row_fourth_max])
    # print("------------maxi =  -----------------")
    # print(maxi)
    # print()
    # print("------------ df.maxValue[i]  =  -----------------")
    # print(df.maxValue[i] )
    df.loc[i, 'maxValue'] = maxi
# print("------------ df.head(10)  =  -----------------")
# print(df.head(50) )
df.to_excel('Column Forces pandas_method1.xlsx', sheet_name='Sheet1', index=False)
