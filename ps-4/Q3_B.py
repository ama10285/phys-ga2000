from pylab import*
import math

def hermite_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * hermite_poly(n - 1, x) - 2 * (n - 1) * hermite_poly(n - 2, x)

def HO_wavefunction(n, x):
    return (exp(-x**2 / 2) * hermite_poly(n, x)) / (sqrt(math.factorial(n) * 2**n * sqrt(pi)))

x_val = linspace(-10, 10, 400)

plot(x_val, HO_wavefunction(30, x_val), label='n=30')

title('Harmonic Oscillator Wavefunction for n=30')
xlabel('x')
ylabel('Wavefunction')
legend()
grid()
show()
