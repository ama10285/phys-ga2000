import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lorenz(state, t, sigma, r, b):
    x, y, z = state
    dxdt = sigma*(y - x)
    dydt = r*x - y - x*z
    dzdt = x*y - b*z
    return [dxdt, dydt, dzdt]

sigma = 10
r = 28
b = 8/3

# Set the initial conditions
state0 = [0, 1, 0]

t = np.arange(0, 50, 0.01)
states = odeint(lorenz, state0, t, args=(sigma, r, b))

x = states[:, 0]
y = states[:, 1]
z = states[:, 2]

plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y')
plt.title('Lorenz Equations: y vs. Time')

plt.figure()
plt.plot(x, z)
plt.xlabel('x')
plt.ylabel('z')
plt.title('Lorenz Equations: z vs. x')
plt.show()
