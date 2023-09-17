from math import*
import cmath as cm
def quadsolve(a,b,s):
    #lets have a discriminant factor
    d = b**2-4*a*c
    if d==0:
        print("The equation has equal roots ")
        x12=-b/(2*a)  #method a
        x34 =(-2*c)/b #method b
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x12,"\n","x2_a=",x12,"\n Using method (b) the roots are the following: \n","x1_b=",x34,"\n","x2_b=",x34)
        return (x12,x12,x34,x34)
    elif d>0:
        print("The equation has real roots ")
        x1=(-b+sqrt(d))/(2*a) 
        x2=(-b-sqrt(d))/(2*a)
        x3=(-2*c)/(b+sqrt(d))
        x4=(-2*c)/(b-sqrt(d))        
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x1,"\n","x2_a=",x2,"\n Using method (b) the roots are the following: \n","x1_b=",x3,"\n","x2_b=",x4)
        return (x1,x2,x3,x4)
    else:
        print("The equation has complex roots ")
        x1c=(-b+cm.sqrt(d))/(2*a)  #or we can write (-b+cm.sqrt(d))(2*a)
        x2c=(-b-cm.sqrt(d))/(2*a) 
        x3c=(-2*c)/(b+cm.sqrt(d))
        x4c=(-2*c)/(b-cm.sqrt(d))
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x1c,"\n","x2_a=",x2c,"\n Using method (b) the roots are the following: \n","x1_b=",x3c,"\n","x2_b=",x4c) 
        return (x1c,x2c,x3c,x4c)


a = 0.001 ; b = 1000 ; c = 0.001
x1,x2,x3,x4= quadsolve(a,b,c)