#  对Column Forces.xlsx从第5行起,计算5-9行的[P	V	M	T]的最大值。间隔8行类推
import pandas as pd  # 导入python的padans工具包。padans是python中专门做数据处理的工具包
df = pd.read_excel("Column Forces.xlsx",sheet_name='Sheet2') #读取Sheet2,定义变量df,存放excel的数据，可以认为将excel转为矩阵。
df.info() # 打印矩阵信息。没有其他作用。
df['maxValue']=0 #增加空值列
df['maxValue所在行']=None #增加空值列
df['maxValue所在列']=None #增加空值列
rows = len(df.axes[0])  # 得到总行数
for i in range(4,rows,8): #从第5行开始到文件末尾，每隔8行一个循环
    df4_4 = df.iloc[i:i+4,-7:-3] # 取得连续4行[P	V	M	T]矩阵，即4x4的矩阵
    maxi = df4_4.stack().max()   # 获取矩阵最大值
    df.loc[i, 'maxValue'] =maxi  #   写excel表的"maxValue" 字段
    listXY = df4_4.stack().idxmax()  # 获取最大值所在坐标，返回一个数组
    X = listXY[0]
    Y = listXY[1]
    df.loc[i, 'maxValue所在行'] = df.loc[X, 'STORY'] + '/' + df.loc[X, '编号']  + '/' + df.loc[X, '工况.1']  # 写excel表的"maxValue所在行" 字段
    df.loc[i, 'maxValue所在列'] = Y  # 写excel表的"maxValue所在列" 字段
df.to_excel('Column Forces pandas_version3.xlsx', sheet_name='Sheet1', index=False) #创建新的excel表
