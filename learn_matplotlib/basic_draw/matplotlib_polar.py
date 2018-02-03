import numpy as np
import matplotlib.pyplot as plt

N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = 2 * np.pi / 20
# width = np.pi / 4 * np.random.rand(N)

print(theta)
print(radii)
print(width)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)

plt.show()
