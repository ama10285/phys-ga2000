from pylab import*

def f(x):
    return x * (x - 1)

def diff_lim(x, h):
    df = (f(x + h) - f(x)) / h
    return df

exact = 1  # exact value of derivative

x = 1
H = [10**-2, 10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14]
abs_error = []
for h in H:
    ak = abs(diff_lim(x, h) - exact) 
    abs_error.append(ak)

figure(figsize=(10, 6))
loglog(H, abs_error, marker='o')
title('Accuracy of Derivative Calculation vs. Delta x')
xlabel('Delta x (Δx)')
ylabel('Absolute Error')
grid()
show()
