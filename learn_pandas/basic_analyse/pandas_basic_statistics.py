import pandas as pd
import numpy as np

a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'])
print(a)
print(b)
# .sum() 计算数据的总和，按0轴计算，下同
print('sum()-------')
print(a.sum())
print(b.sum())
print('------------')
# .count() 非NaN值的数量
print('count()-----')
print(a.count())
print(b.count())
print('------------')
# .mean() .median() 计算数据的算术平均值、算术中位数
print('mean()------')
print(a.mean())
print(b.mean())
print('------------')
print('median()----')
print(a.median())
print(b.median())
print('------------')
# .var()  .std() 计算数据的方差、标准差
print('var()-------')
print(a.var())
print(b.var())
print('------------')
print('std()-------')
print(a.std())
print(b.std())
print('------------')
# .min()  .max() 计算数据的最小值、最大值
print('min()-------')
print(a.min())
print(b.min())
print('------------')
print('max()-------')
print(a.max())
print(b.max())
print('------------')

print('++++++++++++')
print('------------')
# .describe() 针对0轴(各列)的统计汇总
a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print(a.describe())
# Series.describe()的类型是Series
print(a.describe()['count'])
print('------------')
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'])
print(b.describe())
print(b.describe().ix['count'])
