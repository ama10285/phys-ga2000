from math import *
import cmath as cm
def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d == 0:
        x1_a = -b / (2*a)  
        x2_a = x1_a  
        x1_b = -2*c / b  
        x2_b = x1_b  
    elif d > 0:
        x1_a = (-b + sqrt(d)) / (2*a)
        x2_a = (-b - sqrt(d)) / (2*a)
        x1_b = -2*c / (b + sqrt(d))
        x2_b = -2*c / (b - sqrt(d))
    else:
        x1_a = (-b + cm.sqrt(d)) / (2*a)
        x2_a = (-b - cm.sqrt(d)) / (2*a)
        x1_b = -2*c / (b + cm.sqrt(d))
        x2_b = -2*c / (b - cm.sqrt(d))

    diff_a = abs(x1_a - x2_a)
    diff_b = abs(x1_b - x2_b)

    if diff_a < diff_b:
        return (x1_a, x2_a)
    else:
        return (x1_b, x2_b)

