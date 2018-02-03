import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate_l, lstrain = wavfile.read('resources/L1_Strain.wav')
rate_h, hstrain = wavfile.read('resources/H1_Strain.wav')
reftime, ref_H1 = np.genfromtxt('resources/wf_template.txt').transpose()

ltime_interval = 1 / rate_l
htime_interval = 1 / rate_h

ltime_len = lstrain.shape[0] / rate_l
ltime = np.arange(-ltime_len / 2, ltime_len / 2, ltime_interval)
htime_len = hstrain.shape[0] / rate_h
htime = np.arange(-htime_len / 2, htime_len / 2, htime_interval)

fig = plt.figure(figsize=(12, 6))

plth = fig.add_subplot(2, 2, 1)
plth.plot(htime, hstrain, 'y')
plth.set_xlabel('Time (seconds)')
plth.set_ylabel('H1_Strain')
plth.set_title('H1_Strain')

pltl = fig.add_subplot(2, 2, 2)
pltl.plot(ltime, lstrain, 'g')
pltl.set_xlabel('Time (seconds)')
pltl.set_ylabel('L1_Strain')
pltl.set_title('L1_Strain')

pltref = fig.add_subplot(2, 1, 2)
pltref.plot(reftime, ref_H1)
pltref.set_xlabel('Time (seconds)')
pltref.set_ylabel('Template_Strain')
pltref.set_title('Template_Strain')

fig.tight_layout()

plt.show()
plt.close(fig)
