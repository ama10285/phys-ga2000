from math import*
import cmath as cm
def method_A(a,b,c):
    #lets have a discriminant factor
    d = b**2-4*a*c
    if d==0:
        x12=-b/(2*a) 
        return (x12, x12)
    elif d>0:
        x1=(-b+sqrt(d))/(2*a) 
        x2=(-b-sqrt(d))/(2*a)
        return (x1, x2)
    else:
        x1_=(-b+cm.sqrt(d))/(2*a) 
        x2_=(-b-cm.sqrt(d))/(2*a) 
        return (x1_, x2_)

def method_B(a,b,c):
    #lets have a discriminant factor
    d = b**2-4*a*c
    if d==0:
        x12 =(-2*c)/b
        return (x12, x12)
    elif d>0:
        x1=(-2*c)/(b+sqrt(d))
        x2=(-2*c)/(b-sqrt(d)) 
        return (x1, x2)       
    else:
        x1_=(-2*c)/(b+cm.sqrt(d))
        x2_=(-2*c)/(b-cm.sqrt(d))
        return (x1_, x2_)


def quadratic(a,b,c):
    x1a,x2a = method_A(a,b,c)
    x1b,x2b = method_B(a,b,c)
    if log(abs(x1a))>0:
        x1 = x1a
    else:
        x1 = x1b
    if log(abs(x2a))>0:
        x2 = x2a
    else:
        x2 = x2b
    return (x1,x2)


    

