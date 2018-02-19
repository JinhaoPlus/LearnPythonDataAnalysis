import pandas as pd
import numpy as np

# 累计计算
print('累计计算--------------------------')
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'])
print(b)
# .cumsum() 依次给出前1、2、...、n个数的和
print(b.cumsum())
# .cumprod() 依次给出前1、2、...、n个数的积
print(b.cumprod())
# .cummax() 依次给出前1、2、...、n个数的最大值
print(b.cummax())
# .cummin() 依次给出前1、2、...、n个数的最小值
print(b.cummin())

print('滚动计算--------------------------')

# 滚动计算(窗口计算)
b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['a', 'b', 'c', 'd'])
print(b)
# .rolling(w).sum() 依次计算相邻w个元素的和
print(b.rolling(2).sum())
# .rolling(w).mean() 依次计算相邻w个元素的算术平均值
print(b.rolling(3).mean())
# .rolling(w).var() 依次计算相邻w个元素的方差
print(b.rolling(3).var())
# .rolling(w).std() 依次计算相邻w个元素的标准差
print(b.rolling(3).std())
# .rolling(w).min() .max() 依次计算相邻w个元素的最小值和最大值
print(b.rolling(3).min())
print(b.rolling(3).max())
