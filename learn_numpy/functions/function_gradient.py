import numpy as np

# np.gradient(f) 计算数组f中元素的梯度，当f为多维时，返回每个维度梯度
a = np.random.randint(0, 20, (5,))
print(a)
# XY坐标轴连续三个X坐标对应的Y轴值:a, b, c
# b的梯度是: (c‐a)/2
# a的梯度是: (b-a)/1
# c的梯度是: (c-b)/1
print(np.gradient(a))

a = np.random.randint(0, 20, (3, 5))
print(a)
gd = np.gradient(a)
print(gd)
# 0维的梯度
print(gd[0])
# 1维的梯度
print(gd[1])
