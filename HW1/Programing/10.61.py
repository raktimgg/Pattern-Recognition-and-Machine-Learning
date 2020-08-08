import numpy as np
import matplotlib.pyplot as plt

nos = 100000
x = np.random.uniform(0,1,nos)
y = x**3
x2 = np.linspace(0,1,100)
y2 = (1/3)*x2**(-2/3)
plt.hist(y,bins = 100,histtype = 'step',density = True,label = 'PDF from Distribution')   ########## Plotting the density function
plt.plot(x2,y2,label = 'True PDF')
plt.legend()
plt.show()
