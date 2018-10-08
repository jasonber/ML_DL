# US_Baby_Names
import pandas as pd
import numpy as np

baby_name = pd.read_csv('/home/zhangzhiliang/Documents/Book/coding/pandas_exercises/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

# 看前10行
baby_name.head(10)

# 删除 Unnamed 和 Id两列
# del baby_name['Unnamed: 0'] 一次只能删除一个
baby_name.drop(columns=['Unnamed: 0', 'Id'], inplace=True)

# 男性多还是女性多
baby_name['Gender'].value_counts()

# 使用姓名分组， 并命名为名字
names = baby_name.groupby('Name')['Count'].sum().to_frame().sort_values(by='Count', ascending=False)

# 数据中有多少不同的名字
baby_name['Name'].nunique()

# 出现最多的名字
names[names['Count'] == names['Count'].max()]

# 出现最少的名字
names[names['Count'] == names['Count'].min()]

# 中位数
names[names['Count'] == names['Count'].median()]
# 标准差
names['Count'].std()
# 描述统计
names.describe()

# Wind statistic
import pandas as pd
import datetime

data = pd.read_table('/home/zhangzhiliang/Documents/Book/coding/pandas_exercises/06_Stats/Wind_Stats/wind.data',
                     sep = "\s+", parse_dates = [[0, 1, 2]])

# 修正年份
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)
data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# 用年月日作为标签，年月日格式为datetime64[ns]
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data = data.set_index('Yr_Mo_Dy')

# 计算表中的缺失值
data.isnull().sum()

# 非缺失值有多少
data.notnull().sum()

# 所有地点时间的平均风速
data.