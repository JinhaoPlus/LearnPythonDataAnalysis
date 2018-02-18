import pandas as pd
import numpy as np

# 算术运算根据行列索引，补齐后运算，运算默认产生浮点数 补齐时缺项填充NaN (空值)
# 二维和一维、一维和零维间为广播运算
# 采用+ ‐ * /符号进行的二元运算产生新的对象

a = pd.DataFrame(np.arange(12).reshape(3, 4))
b = pd.DataFrame(np.arange(20).reshape(4, 5))
print(a)
print(b)
print(a + b)
print(a * b)
print(b.add(a, fill_value=100))
print(b.mul(a, fill_value=0))

print('----------------------')

b = pd.DataFrame(np.arange(20).reshape(4, 5))
c = pd.Series(np.arange(4))
print(b)
print(c)
print(c - 10)
print(b - c)
print(b.sub(c, axis=0))
print(b.sub(c, axis=1))

# 不同维度间为广播运算，一维Series默认在轴1参与运算
## 0维对1维的运算作用在1维的每一个元素上
## 1维对2维的运算把1维上的列去与2维上的每1行做运算，其实就是把1维作用到2维的每一行上

print('------------------------')

# 比较运算只能比较相同索引的元素，同维度运算，尺寸不一致也不进行补齐直接报错
# 二维和一维、一维和零维间为广播运算
# 采用> < >= <= == !=等符号进行的二元运算产生布尔对象
a = pd.DataFrame(np.arange(12).reshape(3, 4))
d = pd.DataFrame(np.arange(12, 0, -1).reshape(3, 4))
print(a)
print(d)
print(a > d)
print(a == d)

print('------------------------')
a = pd.DataFrame(np.arange(12).reshape(3, 4))
c = pd.Series(np.arange(4))
print(a)
print(c)
print(a > c)
print(c > 0)
