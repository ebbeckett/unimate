from statistics import mean
import numpy as np
import matplotlib.pyplot as plt



rows = [1, 2, 3, 4, 5]
fitnessFunctionA = np.load('abtestnumpy.npy') 
fitnessFunctionB = np.load('abtestnumpyb.npy') 

meanOfA = np.mean(fitnessFunctionA, axis=1)
meanOfB = np.mean(fitnessFunctionB, axis=1)
stdOfA = np.std(fitnessFunctionA, axis=1)
stdOfB = np.std(fitnessFunctionB, axis=1)

meanPlusStdA = (meanOfA + (stdOfA))
meanMinusStdA = (meanOfA - (stdOfA))
meanPlusStdB = (meanOfB + (stdOfB))
meanMinusStdB = (meanOfB - (stdOfB))

plt.plot(meanPlusStdA, label='ROBOT A (mean+std)')
plt.plot(meanOfA, label='ROBOT A (mean)')
plt.plot(meanMinusStdA, label='ROBOT A (mean-std)')

plt.plot(meanPlusStdB, label='ROBOT B (mean+std)')
plt.plot(meanOfB, label='ROBOT B (mean)')
plt.plot(meanMinusStdB, label='ROBOT B (mean-std)')


# plt.plot(stdOfA, label)
# plt.plot(meanOfB, label='ROBOT B')

# for col in range(fitnessFunctionA.shape[1]):
#     plt.plot(rows, fitnessFunctionA[:, col], label='(A)generation'+str(col+1))
    
# for col in range(fitnessFunctionB.shape[1]):
#     plt.plot(rows, fitnessFunctionB[:, col], label='(B)generation'+str(col+1))

plt.legend()
plt.show()