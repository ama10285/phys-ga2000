from pylab import*
import numpy as np
from scipy import integrate
from scipy.integrate import fixed_quad

V = 1000e-6  # vol
p = 6.022e28  # number density
k_B = 1.38e-23  # Boltzmann's const
theta_D = 428  # Debye temp

def int_part(x):
    return x**4 * exp(x) / (exp(x) - 1)**2

def cv(T, N):
    x = theta_D / T
    int_res, _ = fixed_quad(lambda x: int_part(x), 0, x, n=N)
    Cv = 9 * V * p * k_B * (T / theta_D)**3 * int_res
    return Cv

fixed_temperature = 500
N_values = [10, 20, 30, 40, 50, 60, 70]

Cv_values = [cv(fixed_temperature, N) for N in N_values]
plot(N_values, Cv_values, marker="o")

xlabel('Temperature (K)')
ylabel('Heat Capacity (J/K)')
title('Solid Aluminum (Al) Heat Capacity ')
grid()
show()