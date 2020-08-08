import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

nos = 100000
bins = np.linspace(-10, 12, 30)
X = np.random.normal(1,2,nos)
plt.hist(X,bins = 200,histtype = 'step',density = True,label = 'PDF from Distribution') ############# Plotting the density function
x1 = np.linspace(-10,12,10000)
y1 = (1/np.sqrt(2*np.pi*4))*np.exp(-(x1-1)**2/8)
plt.plot(x1,y1,label = 'True PDF')
plt.legend()
plt.grid()
plt.show()
