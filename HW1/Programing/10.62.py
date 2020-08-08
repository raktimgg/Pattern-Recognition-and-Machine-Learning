import numpy as np
import matplotlib.pyplot as plt

nos = 100000
bins = np.linspace(-10, 10, 200)
x = np.random.uniform(0,1,nos)
y = x**3
x2 = np.linspace(0,1,100)
y2 = x2**(1/3)
plt.hist(y,bins = 100,histtype = 'step',cumulative = True, normed = True,label ='CDF from Distribution') ########### Plotting CDF
plt.plot(x2,y2,label = 'True CDF')
plt.legend()
plt.show()
