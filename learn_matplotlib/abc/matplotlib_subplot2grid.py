import numpy as np
import matplotlib.pyplot as plt


def increase(t):
    return 2 * t


def decrease(t):
    return 2 - 2 * t


a = np.arange(0.0, 5.0, 0.02)

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot(a, increase(a))
ax1.plot(a, decrease(a))

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax2.plot(a, increase(a))
ax2.plot(a, decrease(a))

ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax3.plot(a, increase(a))
ax3.plot(a, decrease(a))

ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.plot(a, increase(a))
ax4.plot(a, decrease(a))

ax5 = plt.subplot2grid((3, 3), (2, 1))
ax5.plot(a, increase(a))
ax5.plot(a, decrease(a))

plt.show()
