import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()
ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
ax.set_title('Simple Scatter')

plt.show()
