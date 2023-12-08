import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

L=1e-8  ;x0 = L/2 ;sigma = 1e-10 ; k = 5e10 ;hbar = 1.0545718e-34
N = 1000 ;T = 1e-16 ;L = 1e-8  ;m_e = 9.10938356e-31  ;dt = 1e-18        
def cn_method(N, T, L, m, dt, psi0=None):
    dx = L / (N - 1)
    x = np.linspace(0, L, N)
    t = np.linspace(0, T, N)
    A = np.empty((3, N-2), dtype=complex)
    B = np.empty((3, N-2), dtype=complex)
    a2 = -0.25j * hbar*dt / (m * dx**2)
    a1 = 1 + 1j *hbar* dt / (2 * m * dx**2)
    b2 = 0.25j * hbar*dt / (m * dx**2)
    b1 = 1 - 1j *hbar* dt / (2 * m * dx**2)
    A[0, :] = a2 * np.ones(N-2)  
    A[1, :] = a1 * np.ones(N-2) 
    A[2, :] = a2 * np.ones(N-2)  
    B[0, :] = b2 * np.ones(N-2)  
    B[1, :] = b1 * np.ones(N-2)  
    B[2, :] = b2 * np.ones(N-2)  
    if psi0 is None:
        psi0 = np.exp(-(x[1:-1]-x0)**2/2/sigma**2)*np.exp(1j*k*x[1:-1])

    psi = np.zeros((N, N), dtype=complex)
    psi[0, 1:-1] = psi0

    for n in range(N - 1):
        r = psi[n, 1:-1]
        psi[n + 1, 1:-1] = solve_banded((1, 1), A, r)
    return psi, x, t

psi_final, x, t = cn_method(N, T, L, m_e, dt)

for i in range(0, N, N // 10):
    psi_normalized = np.real(psi_final[i, 1:-1]) / np.max(np.abs(psi_final))
    psi_normalized = np.concatenate([[0], psi_normalized, [0]])  
    plt.plot(x, psi_normalized, label=f' time {t[i]:.2e}')

plt.title('Normalized real part of wavefunction for diffeernt times')
plt.xlabel('Position (x)')
plt.ylabel('Normalized real part of wavefunction')
plt.legend()
plt.show()