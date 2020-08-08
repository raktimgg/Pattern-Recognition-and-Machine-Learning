import numpy as np
import matplotlib.pyplot as plt

N = 5 ## No. of realizations
nos = 50 ## No. of Time Samples per realisation
X = np.empty([N,nos])
for i in range(0,X.shape[1]):
	for j in range (0,X.shape[0]):
		X[j,i] = np.random.normal(0,1)*np.cos(2*np.pi*i)

plt.plot(X.T, label = 'Some realisations of the random process')
plt.xlabel('$t$')
plt.show()