from pylab import*

N =20

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

def v(x):
    return x**4

def calc_period(Amp):
    m = 1
    a = 0
    b = Amp
    x,w = gaussxwab(N,a,b)
    s = 0
    for i in arange(N):
        s += w[i]/sqrt(v(b)-v(x[i]))
    return s*sqrt(8*m)

amp_vals = arange(0.01,2.01,0.01)

P = [calc_period(a) for a in amp_vals]

plot(amp_vals, P)
xlabel('Amplitude (a)')
ylabel('T (s)')
title('Period vs Amplitude for anharmonic oscillator')
grid()
show()