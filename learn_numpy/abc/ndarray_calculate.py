import numpy as np

# 标量运算 数组与标量之间的运算作用于数组的每一个元素
a = np.array([-1.1, 2.2, -3.3, 4.4, -5.5, 6.6, -7.7, 8.8, -9.9])
b = np.array([1.1, -2.2, 3.3, -4.4, 5.5, -6.6, 7.7, -8.8, 9.9])
# 一元运算
print('[Part1]--------------')
print('*2:', a * 2)
# np.abs(x) np.fabs(x) 计算数组各元素的绝对值
print('abs:', np.abs(a))
print('fabs:', np.fabs(a))
# np.sqrt(x) 计算数组各元素的平方根
print('sqrt:', np.sqrt(np.abs(a)))
# np.square(x) 计算数组各元素的平方
print('square:', np.square(a))
# np.log(x) np.log10(x) np.log2(x) 计算数组各元素的自然对数、10底对数和2底对数
print('log:', np.log(np.abs(a)))
# np.ceil(x) np.floor(x) 计算数组各元素的ceiling值 或 floor值
print('ori:', a)
print('ceil:', np.ceil(a))
print('floor:', np.floor(a))
# np.rint(x) 计算数组各元素的四舍五入值
print('rint:', np.rint(a))
# np.modf(x) 将数组各元素的小数和整数部分以两个独立数组形式返回
print('modf:', np.modf(a))
# np.cos(x) np.cosh(x) np.sin(x) np.sinh(x) np.tan(x) np.tanh(x) 计算数组各元素的普通型和双曲型三角函数
print('cos:', np.cos(a))
# np.exp(x) 计算数组各元素的指数值
print('exp:', np.exp(a))
# np.sign(x) 计算数组各元素的符号值，1(+), 0, ‐1(‐)
print('sign:', np.sign(a))

# 二元运算
print('[Part2]--------------')
# + ‐ * / ** 两个数组各元素进行对应运算
print(a + b)
# np.maximum(x,y) np.fmax() np.minimum(x,y) np.fmin() 元素级的最大值/最小值计算
print(np.maximum(a, b))
# np.mod(x,y)  元素级的模运算
print(np.mod(a, b))
# np.copysign(x,y)  将数组y中各元素值的符号赋值给数组x对应元素
print(np.copysign(a, b))
# > < >= <= == != 算术比较，产生布尔型数组
print(a > b)
