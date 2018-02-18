import pandas as pd
import numpy as np

# DataFrame类型的创建
# 二维ndarray对象
d = pd.DataFrame(np.arange(10).reshape(2, 5))
print(d)
# 由一维ndarray对象构成的字典
dt = {'one': np.arange(5), 'two': np.arange(5)}
print(pd.DataFrame(dt, index=['a', 'b', 'c', 'd', 'e']))
# 由列表构成的字典
dl = {'one': [1, 2, 3],
      'two': [4, 5, 6]}
print(pd.DataFrame(dl))
# 由元组构成的字典
dl = {'one': (1, 2, 3),
      'two': (4, 5, 6)}
print(pd.DataFrame(dl))
# 由字典构成的字典
dd = {'one': {'a': 1, 'b': 2, 'c': 3},
      'two': {'a': 4, 'b': 5, 'c': 6}}
print(pd.DataFrame(dd))
# 由Series对象构成的字典
dt = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'e']),
      'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(dt))
print(pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three']))

# DataFrame类型是带标签的二维数组：所以要用字典来创建
# 字典的key是columns
# 字典的value是字典的时候value字典的key是index
# 字典的value是列表或者元组的时候默认使用0，1，2来作为index
# 字典的value是Series对象的时候可以设定index


# DataFrame基本操作
dl = {'城市': ['北京', '上海', '广州', '深圳', '沈阳'],
      '环比': [101.5, 101.2, 101.3, 102.0, 100.1],
      '同比': [120.7, 127.3, 119.4, 140.9, 101.4],
      '定基': [121.4, 127.8, 120.0, 145.5, 101.6]}
d = pd.DataFrame(dl, index=['c1', 'c2', 'c3', 'c4', 'c5'])
print(d)
print(d.index)
print(d.columns)
print(d.values)
print(d['同比'])
print(d['同比']['c2'])
