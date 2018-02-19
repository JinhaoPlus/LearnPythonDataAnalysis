import pandas as pd
import numpy as np

# 索引排序：进行排序是索引，把索引按照大小进行排序，值随索引的排序而变化
# .sort_index()方法在指定轴上根据索引进行排序，默认0轴(纵向)，默认升序
# .sort_index(axis=0, ascending=True)

b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
print(b)
print(b.sort_index())
print(b.sort_index(ascending=False))
print(b.sort_index(axis=1, ascending=False))

print('----------------------------')

# 值排序：进行排序的是值，把值按照大小进行排序，索引随值的排序而变化
# .sort_values()方法在指定轴上根据数值进行排序，默认0轴(纵向)，默认升序
# Series.sort_values(axis=0, ascending=True)
# DataFrame.sort_values(by, axis=0, ascending=True)
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
print(b)
# 排序第2列的值影响了0轴列索引，其他列的数据也因此发生了变化
print(b.sort_values(2, ascending=False))
# 排序第'a'行的值影响了1轴行索引，其他行的数据也因此发生了变化
print(b.sort_values('a', axis=1, ascending=False))

print('-----------------------------')

# NaN统一放到排序末尾
a = pd.DataFrame(np.arange(12).reshape(3, 4), index=['a', 'b', 'c'])
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
c = a + b
print(c)
print(c.sort_values(2, ascending=False))
