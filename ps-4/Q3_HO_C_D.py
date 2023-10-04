from pylab import *
import math
from scipy.special import roots_hermite
import numpy as np
def gaussxw(N):
    a = linspace(3, 4 * N - 1, N) / (4 * N + 2)
    x = cos(pi * a + 1 / (8 * N * N * tan(a)))
    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p0 = ones(N, float)
        p1 = copy(x)
        for k in range(1, N):
            p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = max(abs(dx))
    w = 2 * (N + 1) * (N + 1) / (N * N * (1 - x * x) * dp * dp)
    return x, w

def gaussxwab(N, a, b):
    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    return xp, wp

def hermite_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite_poly(n - 1, x) - 2 * (n - 1) * hermite_poly(n - 2, x)
    
def HO_wavefunction(n, x):
    return (exp(-x**2 / 2) * hermite_poly(n, x)) / (sqrt(math.factorial(n) * 2**n * sqrt(pi)))
# Gaussian Quadrature
a = -1 ;b = 1 ;N = 100
z,w = gaussxwab(N,a,b)
uc_gq = 0.
nn =5
for k in arange(N):
    uc_gq += w[k]*((1 + z[k]**2)/(1-z[k]**2)**2)*((HO_wavefunction(nn,(z[k]/(1-z[k]**2))))**2)*((z[k]/(1-z[k]**2))**2)
print("Uncertainty using Gauass Quadrature =",sqrt(uc_gq))

# Gauss-Hermite Quadrature
NN = 80
xh,wh = roots_hermite(NN)
#xh,wh = np.polynomial.hermite.hermgauss(NN)
uc_gh = 0.
for i in arange(NN):
    uc_gh += wh[i]*(xh[i]**2)*hermite_poly(nn,xh[i])**2
print("Uncertainty using Gauss Hermite Quadrature =",sqrt(uc_gh/(math.factorial(5)*sqrt(pi)*(2**5))))
