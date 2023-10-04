from pylab import*
import numpy as np
from scipy import integrate

V = 1000e-6  # vol
p = 6.022e28  # number density
k_B = 1.38e-23  # Boltzmann's const
theta_D = 428  # Debye temp

def int_part(x):
    return x**4 * exp(x) / (exp(x) - 1)**2

def cv(T, N=50):
    x = theta_D / T
    int_res, _ = integrate.quad(lambda x: int_part(x), 0, x, points=linspace(0, x, N))
    Cv = 9 * V * p * k_B * (T / theta_D)**3 * int_res
    return Cv

Ts = linspace(5, 500, 100)
hc = []
for T in Ts:
    hc.append(cv(T))
plot(Ts, hc)
xlabel('Temperature (K)')
ylabel('Heat Capacity (J/K)')
title('Solid Aluminum (Al) Heat Capacity ')
grid()
show()
