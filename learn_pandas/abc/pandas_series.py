import pandas as pd
import numpy as np

# Series创建
# Python列表，index与列表元素个数一致
a = pd.Series([9, 8, 7, 6])
print('a=\n', a)
b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print('b=\n', b)
# 标量值，index表达Series类型的尺寸
c = pd.Series(25, index=['a', 'b', 'c', 'd'])
print('c=\n', c)
# Python字典，键值对中的“键”是索引，index从字典中进行选择操作
d = pd.Series({'a': 9, 'b': 8, 'c': 7, 'd': 6})
print('d=\n', d)
e = pd.Series({'a': 9, 'b': 8, 'c': 7, 'd': 6}, index=['d', 'c', 'b', 'a', 'x'])
print('e=\n', e)
# ndarray，索引和数据都可以通过ndarray类型创建
f = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print('f=\n', f)
g = pd.Series(np.arange(5), index=np.arange(9, 4, -1))
print('g=\n', g)
# 其他函数，range()函数等
h = pd.Series(range(10))
print('g=\n', h)

# Series基本操作
a = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])
print('a=\n', a)
# 取索引
print(a.index)
# 取值
print(a.values)
# 自动索引和自定义索引并存
print(a[0])
print(a['a'])

# Series类型的操作类似ndarray类型
# 索引方法相同，采用[]
print(a[3])
# NumPy中运算和操作可用于Series类型
print(np.exp(a))
# 切片:可以通过自动索引或自定义索引的列表进行切片
# 两套索引并存，但不能混用: 无法取到print(a[['b', 'c', 3]])
print(a[:3])
print(a[['b', 'c', 'd']])
print(a[a > a.median()])

# Series类型的操作类似Python字典类型:
# 通过自定义索引访问
print(a[0])
# 保留字in操作
print('c' in a)
print(0 in a)
# 使用.get()方法
print(a.get('c', 0))

# 对齐操作：Series类型在运算中会自动对齐不同索引的数据
a = pd.Series([9, 8, 7], index=['a', 'b', 'c'])
b = pd.Series([1, 2, 3, 4], index=['b', 'c', 'd', 'e'])
print(a + b)

# name属性
a = pd.Series([9, 8, 7], index=['a', 'b', 'c'])
a.name = 'Series对象a'
a.index.name = '索引'
print(a)
