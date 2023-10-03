import numpy as np
from pylab import*
from scipy.integrate import quad

def v(x):
    return x**4

def integrand(x, E, m):
    return 1 / sqrt(2 * (E - v(x)) / m)

def calculate_period(amplitude):
    E = v(amplitude)
    m = 1 
    integral_result, _ = quad(integrand, 0, amplitude, args=(E, m))
    return 4 * integral_result

amplitudes = linspace(0, 2, 100)
periods = []
for amplitude in amplitudes:
    period = calculate_period(amplitude)
    periods.append(period)

plot(amplitudes, periods)
xlabel('Amplitude (a)')
ylabel('Period (T)')
title('Period vs Amplitude for anharmonic oscillator')
grid()
show()