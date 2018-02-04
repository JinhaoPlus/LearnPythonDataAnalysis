import numpy as np

# a.tofile(frame, sep='', format='%s')
a = np.arange(100).reshape(5, 10, 2)
a.tofile('target/a.data', sep=',', format='%d')
# sep=''(sep的默认值)的时候即按照二进制方式把数组元素放进去
# 所谓二进制，即不是把每个元素按照一定的字符编码方式编码成相应的字符存储，
# 而是直接把数字元素放到64bit(OS的存储单元)中去存储，不做字符编码
a.tofile('target/ab.data', format='%d')
# np.fromfile(frame, dtype=float, count=‐1, sep='')
b = np.fromfile('target/a.data', dtype=np.int, sep=',')
print(b)
c = np.fromfile('target/a.data', dtype=np.int, sep=',').reshape(5, 10, 2)
print(c)
d = np.fromfile('target/ab.data', dtype=np.int).reshape(5, 10, 2)
print(d)

# 该方法需要读取时知道存入文件时数组的维度和元素类型
# a.tofile()和np.fromfile()需要配合使用
# 可以通过元数据文件来存储额外信息
