from pylab import*

V = 1000e-6  
p = 6.022e28  
k_B = 1.38e-23 
theta_D = 428 

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

def integrand(x):
    return x**4 * exp(x) / (exp(x) - 1)**2

def cv(T, N):
    b = theta_D / T
    a = 0.
    x,w = gaussxwab(N,a,b)
    s = 0.  
    for k in arange(N):
        s += w[k]*integrand(x[k])
    return s*9 * V * p * k_B * (T / theta_D)**3 

T_values = arange(5,500,0.1)
N_values = arange(1,101)

fixed_temp=100
N =50

Cv_T = [cv(T,N) for T in T_values]
Cv_N = [cv(fixed_temp,N) for N in N_values]

plot(T_values,Cv_T) 
xlabel('Number of Quadrature Points (N)')
ylabel('Heat Capacity (J/K)')
title('Solid Aluminum (Al) Heat Capacity')
grid()
show()

plot(N_values,Cv_N) 
xlabel('Number of Quadrature Points (N)')
ylabel('Heat Capacity (J/K)')
title(f'Solid Aluminum (Al) Heat Capacity at T = {fixed_temp} K')
grid()
show()