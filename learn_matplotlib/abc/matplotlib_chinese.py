import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.0, 5.0, 0.2)

plt.xlabel(u'横轴：时间')
plt.ylabel(u'纵轴：振幅')
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
