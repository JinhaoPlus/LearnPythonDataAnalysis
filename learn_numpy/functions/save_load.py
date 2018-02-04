import numpy as np

a = np.arange(100).reshape(5, 10, 2)
np.save('target/ar.npy', a)
ar = np.load('target/ar.npy')
print(ar)
