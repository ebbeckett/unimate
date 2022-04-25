import numpy as np
import matplotlib.pyplot as plt



rows = [1, 2, 3, 4, 5]
fitnessFunctionA = np.load('abtestnumpy.npy') 
fitnessFunctionB = np.load('abtestnumpyb.npy') 

for col in range(fitnessFunctionA.shape[1]):
    plt.plot(rows, fitnessFunctionA[:, col], label='(A)generation'+str(col+1))
    

for col in range(fitnessFunctionB.shape[1]):
    plt.plot(rows, fitnessFunctionB[:, col], label='(B)generation'+str(col+1))


#plt.plot(rows, fitnessFunctionA, label='BASE A', linewidth=5)

plt.legend()
plt.show()