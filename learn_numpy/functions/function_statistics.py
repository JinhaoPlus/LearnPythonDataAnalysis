import numpy as np

print('[Part1]---------------')
a = np.arange(16).reshape(2, 2, 4)
print(a)
# sum(a, axis=None) 根据给定轴axis计算数组a相关元素之和，axis整数或元组
print(np.sum(a))
# mean(a, axis=None) 根据给定轴axis计算数组a相关元素的期望，axis整数或元组
print(np.mean(a))
# axis=0，取0维的各元素求期望组成的数组：(a[0]+a[1]+a[2])/3
print('axis=0---------------')
print(np.mean(a, axis=0))
# axis=1，取1维的各元素求期望组成的数组
print('axis=1---------------')
print(np.mean(a, axis=1))
# axis=2，取2维的各元素求期望组成的数组
print('axis=2---------------')
print(np.mean(a, axis=2))
# average(a,axis=None,weights=None)  根据给定轴axis计算数组a相关元素的加权平均值
# 2*10+7*5+1*12/(10+5+1)=4.1875
print('---------------')
print(np.average(a, axis=0, weights=[10, 5]))
# std(a, axis=None) 根据给定轴axis计算数组a相关元素的标准差
print(np.std(a))
# var(a, axis=None) 根据给定轴axis计算数组a相关元素的方差
print(np.var(a))

print('[Part2]---------------')
a = np.arange(15, 0, -1).reshape(3, 5)
print(a)
# min(a) max(a) 计算数组a中元素的最小值、最大值
print(np.min(a))
print(np.max(a))
# argmin(a) argmax(a)  计算数组a中元素最小值、最大值的扁平化降为一维后下标
print(np.argmin(a))
print(np.argmax(a))
# unravel_index(index, shape)  根据shape将一维下标index转换成多维下标
print(np.unravel_index(np.argmax(a), a.shape))
# ptp(a) 计算数组a中元素最大值与最小值的差
print(np.ptp(a))
# median(a) 计算数组a中元素的中位数(中值)
print(np.median(a))
