import numpy as np
import matplotlib.pyplot as plt

# [Part1]
print('[Part1]------------------------')
# rand(d0,d1,..,dn) 根据d0‐dn创建随机数数组，浮点数，[0,1)，均匀分布
a = np.random.rand(3, 4, 5)
print(a)
# randn(d0,d1,..,dn) 根据d0‐dn创建随机数数组，标准正态分布
an = np.random.randn(3, 4, 5)
print(an)
# randint(low[,high,shape]) 根据shape创建随机整数或整数数组，范围是[low, high)
ai = np.random.randint(100, 200, (3, 4))
print(ai)
# seed(s) 随机数种子，s是给定的种子值，随机数种子相同随机出的结果就是相同的
np.random.seed(10)
ai1 = np.random.randint(100, 200, (3, 4))
print(ai1)
np.random.seed(10)
ai2 = np.random.randint(100, 200, (3, 4))
print(ai2)

# [Part2]
print('[Part2]------------------------')
a = np.random.randint(100, 200, (3, 4))
print(a)
# shuffle(a) 根据数组a的第1轴产生一个新的乱序数组，改变数组
np.random.shuffle(a)
print(a)
# permutation(a) 根据数组a的第1轴进行随机排列，不改变数组
b = np.random.permutation(a)
print(a)
print(b)

# [Part3]
print('[Part3]------------------------')
# choice(a[,size,replace,p]) 从一维数组a中以概率p抽取元素，形成size形状新数组
# replace表示是否可以重用元素，默认为False
c = np.random.randint(100, 200, (8,))
print(c)
d1 = np.random.choice(c, (3, 2))
print(d1)
d2 = np.random.choice(c, (3, 2), replace=True)
print(d2)
d3 = np.random.choice(c, (3, 2), p=c / np.sum(c))
print(d3)

# [Part4]
print('[Part4]------------------------')
# uniform(low,high,size) 产生具有均匀分布的数组,low起始值,high结束值,size形状
u = np.random.uniform(0, 10, (1000,))
plt.subplot(2, 2, 1)
plt.hist(u, 100, normed=0, histtype='stepfilled', facecolor='y', alpha=0.75)
# normal(loc,scale,size) 产生具有正态分布的数组,loc均值,scale标准差,size形状
n = np.random.normal(10, 5, (1000,))
plt.subplot(2, 2, 2)
plt.hist(n, 100, normed=0, histtype='stepfilled', facecolor='g', alpha=0.75)
# poisson(lam,size) 产生具有泊松分布的数组,lam随机事件发生率,size形状
p = np.random.poisson(50, (1000,))
plt.subplot(2, 1, 2)
plt.hist(p, 100, normed=0, histtype='stepfilled', facecolor='g', alpha=0.75)
plt.show()
