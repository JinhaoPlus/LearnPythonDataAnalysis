import numpy as np

# CSV (Comma‐Separated Value, 逗号分隔值)
# np.savetxt(frame, array, fmt='%.18e', delimiter=None)
a = np.arange(100).reshape(5, 20)
np.savetxt('target/a.csv', a, fmt='%d', delimiter=',')
np.savetxt('target/af.csv', a, fmt='%.1f', delimiter=',')

# np.loadtxt(frame, dtype=np.float, delimiter=None， unpack=False)
b = np.loadtxt('target/a.csv', delimiter=',')
print(b)
b = np.loadtxt('target/a.csv', dtype=np.int, delimiter=',')
print(b)

# CSV只能有效存储一维和二维数组
# np.savetxt() np.loadtxt()只能有效存取一维和二维数组
