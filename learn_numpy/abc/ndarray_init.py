import numpy as np

# x = np.array(list/tuple, dtype=np.float32)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x)
y = np.array([[1, 2], [9, 8], (0.1, 0.2)])
print(y)

# init function [Group1]
# np.arange(n) 类似range()函数，返回ndarray类型，元素从0到n‐1
ar1 = np.arange(10)
print(ar1)
ar2 = np.arange(0, 1, 0.1, dtype=np.float)
print(ar2)
# np.ones(shape) 根据shape生成一个全1数组，shape是元组类型
ao = np.ones((2, 3))
print(ao)
# np.zeros(shape) 根据shape生成一个全0数组，shape是元组类型
az = np.zeros((2, 3))
print(az)
# np.full(shape,val) 根据shape生成一个数组，每个元素值都是val
av = np.full((2, 3), 2)
print(av)
# np.eye(n) 创建一个正方的n*n单位矩阵，对角线为1，其余为0
ae = np.eye(3)
print(ae)

# init function [Group2]
a_ori = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(a_ori)
# np.ones_like(a) 根据数组a的形状生成一个全1数组
aol = np.ones_like(a_ori)
print(aol)
# np.zeros_like(a) 根据数组a的形状生成一个全0数组
azl = np.zeros_like(a_ori)
print(azl)
# np.full_like(a,val) 根据数组a的形状生成一个数组，每个元素值都是val
afl = np.full_like(a_ori, 5)
print(afl)

# init function [Group3]
# np.linspace() 根据起止数据等间距地填充数据，形成数组
al1 = np.linspace(1, 10, 4)
print(al1)
al2 = np.linspace(1, 10, 4, endpoint=False)
print(al2)
# np.concatenate() 将两个或多个数组合并成一个新的数组
ac = np.concatenate((al1, al2))
print(ac)
