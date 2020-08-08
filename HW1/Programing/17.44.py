import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram

nos = 100000
X = np.random.normal(0,1,nos)


##### Plotted on log scale along the y-axis 
f1, pxx1 = periodogram(X, nfft = 64)
plt.semilogy(f1,pxx1, label = 'N = 64')
f12, pxx2 = periodogram(X, nfft = 128)
plt.semilogy(f12,pxx2, label = 'N = 128')
f3, pxx3 = periodogram(X, nfft = 256)
plt.semilogy(f3,pxx3, label = 'N = 256')
plt.legend()
plt.show()