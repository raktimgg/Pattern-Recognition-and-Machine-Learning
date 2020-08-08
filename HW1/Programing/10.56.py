import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

nos = 100000
U = np.random.uniform(0,1,nos)
X = 1 - np.sqrt(1-U)
plt.hist(X,bins = 100,histtype = 'step',density = True,label = 'PDF from Distribution') ####### Plotting the density function
x2 = np.linspace(0,2,1000)
y2 = np.zeros(x2.shape[0])
y2[:500] = 2 - 2*x2[:500]
y2[500:] = 0
plt.plot(x2,y2,label = 'True PDF')
plt.show()