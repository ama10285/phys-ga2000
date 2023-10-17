from pylab import*
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as linalg

def is_float(string):
    """ True if given string is float else False"""
    try:
        return float(string)
    except ValueError:
        return False

data = []
with open(r'C:\Users\HP-ENVY\Desktop\\signal.dat', 'r') as f:
    d = f.readlines()
    for i in d:
        k = i.rstrip().split('|')
        for i in k:
            if is_float(i):
                data.append(float(i)) 

data = np.array(data, dtype='float')
x = data[::2]/1e9
y = data[1::2]

plt.plot(x, y, 'o')
plt.xlabel('time')
plt.ylabel('signal')
plt.title('Time vs Signal')
plt.show()


A = np.zeros((len(x), 4))
A[:, 0] = 1.
A[:, 1] = x 
A[:, 2] = x**2
A[:, 3] = x**3
(u, w, vt) = np.linalg.svd(A, full_matrices=False)
ainv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
c = ainv.dot(y)
ym = A.dot(c) 
plt.plot(x, y, '.', label='data')
plt.plot(x, ym, '.', label='model')
plt.xlabel('time')
plt.ylabel('signal')
plt.title('Data Fitting using third-order polynomial')
plt.legend()
plt.show()

# Calculate residuals
residuals = y - ym
plt.plot(x, residuals, '.',label='data - model')
plt.xlabel('time')
plt.ylabel('Residuals')
plt.title('Residuals of the Model')
plt.show()



S = np.zeros((len(x), 31))
S[:, 0] = 1.
S[:, 1] = x 
S[:, 2] = x**2
S[:, 3] = x**3
S[:, 4] = x**4
S[:, 5] = x**5
S[:, 6] = x**6
S[:, 7] = x**7
S[:, 8] = x**8
S[:, 9] = x**9
S[:, 10] = x**10
S[:, 11] = x**11
S[:, 12] = x**12
S[:, 13] = x**13
S[:, 14] = x**14
S[:, 15] = x**15
S[:, 16] = x**16
S[:, 17] = x**17
S[:, 18] = x**18
S[:, 19] = x**19
S[:, 20] = x**20
S[:, 21] = x**21
S[:, 22] = x**22
S[:, 22] = x**22
S[:, 24] = x**24
S[:, 25] = x**25
S[:, 26] = x**26
S[:, 27] = x**27
S[:, 28] = x**28
S[:, 29] = x**29
S[:, 30] = x**30

(U, W, VT) = np.linalg.svd(S, full_matrices=False)
ainvv = VT.transpose().dot(np.diag(1. / W)).dot(U.transpose())

C = ainvv.dot(y)
ym2 = S.dot(C) 
plt.plot(x, y, '.', label='data')
plt.plot(x, ym2, '.', label='model')
plt.xlabel('time')
plt.ylabel('signal')
plt.title('Data Fitting using higher-order polynomial (30)')
plt.legend()
plt.show()