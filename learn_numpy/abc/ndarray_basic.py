import numpy as np

# ndarray = N-dimensionality array
# ndarray一般要求所有元素类型相同(同质)，非同质数组性能不佳
# 1-D Array
a1 = np.array([0, 1, 2, 3, 4])
print(a1)
# 2-D Array
a2 = np.array([[0, 1, 2, 3, 4], [9, 8, 7, 6, 5]])
print(a2)
# 秩，即轴的数量或维度的数量
print(a2.ndim)
# ndarray对象的尺度，对于矩阵，n行m列
print(a2.shape)
# ndarray对象元素的个数，相当于.shape中n*m的值
print(a2.size)
# ndarray对象的元素类型
print(a2.dtype)
# ndarray对象中每个元素的大小，以字节为单位
print(a2.itemsize)

