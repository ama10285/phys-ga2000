import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as linalg

# Define the harmonic sequence
num_harmonics = 10
frequencies = np.arange(1, num_harmonics + 1) / (2 * (x[-1] - x[0]))

# Construct the design matrix
S = np.zeros((len(x), 2 * num_harmonics + 1))
S[:, 0] = 1.  # Zero-point offset
for i in range(1, num_harmonics + 1):
    S[:, 2 * i - 1] = np.sin(2 * np.pi * frequencies[i - 1] * x)
    S[:, 2 * i] = np.cos(2 * np.pi * frequencies[i - 1] * x)

# Perform SVD
(U, W, VT) = np.linalg.svd(S, full_matrices=False)
ainvv = VT.transpose().dot(np.diag(1. / W)).dot(U.transpose())

# Calculate coefficients
C = ainvv.dot(y)

# Calculate the model
ym = S.dot(C)

# Plot the data and the model
plt.plot(x, y, '.', label='data')
plt.plot(x, ym,'.', label='model')
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()
plt.show()