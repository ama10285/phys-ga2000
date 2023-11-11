import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brent

def parabolic_step(func=None, a=None, b=None, c=None):
    fa = func(a)
    fb = func(b)
    fc = func(c)
    denom = (b - a) * (fb - fc) - (b - c) * (fb - fa)
    numer = (b - a)**2 * (fb - fc) - (b - c)**2 * (fb - fa)
    if np.abs(denom) < 1.e-15:
        x = b
    else:
        x = b - 0.5 * numer / denom
    return x

def func(x):
    return ((x - 0.3)**2) * np.exp(x)

def optimize():
    golden_section = (3. - np.sqrt(5)) / 2
    a = -1
    b = 1.1
    c = 4
    tol = 1e-7
    flag = True
    err = abs(c - a)
    err_list, b_list = [err], [b]
    while err > tol:
        s = parabolic_step(func=func, a=a, b=b, c=c)
        if (s >= b) or ((flag == True) and (abs(s - c) >= abs(c - b))) or ((flag == False) and (abs(s - c) >= abs(b - c))):
            if (b - a) > (c - b):
                x = b
                b = b - golden_section * (b - a)
            else:
                x = b + golden_section * (c - b)
            fb = func(b)
            fx = func(x)
            if fb < fx:
                c = x
            else:
                a = b
                b = x
            flag = True
        else:
            flag = False
        err = abs(c - a)
        err_list.append(err)
        b_list.append(b)
    print(f'Minimum using Brent Implementation= {b}')
    return b_list, err_list

def plot(b_list, err_list):
    log_err = [np.log10(err) for err in err_list]
    fig, axs = plt.subplots(2, 1, sharex=True)
    ax0, ax1 = axs[0], axs[1]
    ax0.scatter(range(len(b_list)), b_list, marker='o', facecolor='red', edgecolor='k')
    ax0.plot(range(len(b_list)), b_list, 'r-', alpha=.5)
    ax1.plot(range(len(err_list)), log_err, '.-')
    ax1.set_xlabel('number of iterations')
    ax0.set_ylabel(r'$x_{min}$')
    ax1.set_ylabel(r'$\log{\delta}$')
    plt.savefig('convergence.png')

if __name__ == "__main__":
    b_list, err_list = optimize()
    plot(b_list, err_list)

def main():
    result = brent(func)
    print(f'Minimum using Scipy Brent = {result}')
    
if __name__ == "__main__":
    main()

