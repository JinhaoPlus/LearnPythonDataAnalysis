import numpy as np

# 维度变换
# [Part1] 指定维度变换
print('[Part1]-----------------------')
a_ori = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(a_ori)
print(a_ori.shape)
print(a_ori.size)
# .reshape(shape)  不改变数组元素，返回一个shape形状的数组，原数组不变
ars = a_ori.reshape((6, 2))
print(ars)
print(ars.shape)
print(ars.size)
# .resize(shape) 不改变数组元素，返回一个shape形状的数组，原数组改变
print('-----------------------')
print(a_ori)
print(a_ori.shape)
print(a_ori.size)
a_ori.resize((6, 2))
print(a_ori)
print(a_ori.shape)
print(a_ori.size)

print('[Part2]-----------------------')
# [Part2] 对称和转置变换
# .swapaxes(ax1,ax2) 将数组n个维度中两个维度进行调换
# 此例将shape(3,2,2)转换为(2,3,2)，即转换其0维和1维
a_ori = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
asw = a_ori.swapaxes(0, 1)
print(asw)
print(asw.shape)
print('-----------------------')
# .transpose(*axes) 将数组维度按照axes进行调换
# 此例将shape(3,2,2)转换为(2,2,3)，即将(0D,1D,2D)转换为(2D,1D,0D)
a_ori = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
ats = a_ori.transpose(2, 1, 0)
print(ats)
print(ats.shape)
# .flatten() 对数组进行降维，返回折叠后的一维数组，原数组不变
print('-----------------------')
afl = a_ori.flatten()
print(afl)
print(afl.shape)

# 元素类型变换
a_ori = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
# new_a = a.astype(new_type)
# astype()方法一定会创建新的数组(原始数据的一个拷贝)，即使两个类型一致
aty = a_ori = a_ori.astype(np.float)
print(aty)
# ls = a.tolist() ndarray数组向列表的转换
lll = a_ori.tolist()
print(lll)
