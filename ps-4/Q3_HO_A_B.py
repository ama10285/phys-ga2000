from pylab import *
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

# Plot for n=0, 1, 2, 3
x_vals = linspace(-4, 4, 400)
for n in range(4):
    plot(x_vals, HO_wavefunction(n, x_vals), label=f'n={n}')

title('Harmonic Oscillator Wavefunctions (n=0, 1, 2, 3)')
xlabel('x')
ylabel('Wavefunction')
legend()
grid()
show()

# Plot for n=30
x_vals_30 = linspace(-10, 10, 400)
plot(x_vals_30, HO_wavefunction(30, x_vals_30), label='n=30')

title('Harmonic Oscillator Wavefunction for n=30')
xlabel('x')
ylabel('Wavefunction')
legend()
grid()
show()
