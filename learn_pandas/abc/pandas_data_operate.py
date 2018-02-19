import pandas as pd
import numpy as np

# .reindex()能够改变或重排Series和DataFrame索引
dl = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'],
      '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
      '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
      '定基': [121.4, 127.8, 120.0, 145.5, 101.6]}
d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
print(d)
d = d.reindex(index=['c5', 'c4', 'c3', 'c2', 'c1'], columns=['城市', '环比', '同比', '定基'])
print(d)
newc = d.columns.insert(4, '新增')
d = d.reindex(columns=newc, fill_value=200)
print(d)

print('---------------------')

# 索引的常用方法
d = pd.DataFrame({'one': {'a': 1, 'b': 2, 'c': 3},
                  'two': {'a': 4, 'b': 5, 'c': 6}})
# .append(idx) 连接另一个Index对象，产生新的Index对象
# .diff(idx) 计算差集，产生新的Index对象
# .intersection(idx) 计算交集
# .union(idx) 计算并集
# .delete(loc) 删除loc位置处的元素
# .insert(loc,e) 在loc位置增加一个元素e
nc = d.columns.delete(0)
ni = d.index.insert(4, 'd')
nd = d.reindex(index=ni, columns=nc, method='ffill')
print(nd)

print('+++++++++++++++++++++++++++++++')

# reindex的fill-method的使用
# acd里c有gap所以要fill，ffill向前找到b填充，bfill向后找到d填充
# aed里e有gap所以ffill向前找到d填充，向后找不到所以填充了也是NaN
# reindex在指定method的时候必须要要求index是单向递增或者递减序列，否则就会报错：reindex如果index设置成(‘a’, 1, ‘d’)就直接报错了

dd = {'one': {'a': 1, 'b': 2, 'd': 3},
      'two': {'a': 4, 'b': 5, 'd': 6},
      'thr': {'a': 7, 'b': 8, 'd': 9}}
df = pd.DataFrame(dd)
print(df)
print(df.reindex(('a', 'b', 'd'), method='ffill'))
print(df.reindex(('a', 'c', 'd'), method='ffill'))
print(df.reindex(('a', 'c', 'd'), method='bfill'))
print(df.reindex(('a', 'e', 'd'), method='ffill'))
print(df.reindex(('a', 'e', 'd'), method='bfill'))

# .drop()能够删除Series和DataFrame指定行或列索引
print('-----------------------')
d = pd.DataFrame({'one': {'a': 1, 'b': 2, 'c': 3},
                  'two': {'a': 4, 'b': 5, 'c': 6}})
print(d)
print(d.drop('c'))
print(d.drop('two', axis=1))