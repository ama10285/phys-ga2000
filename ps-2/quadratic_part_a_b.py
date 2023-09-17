from math import*
import cmath as cm
def quadsolve(a,b,s):
    #lets have a discriminant factor
    d = b**2-4*a*c
    if d==0:
        print("The equation has equal roots ")
        x1_a=-b/(2*a)  #method a
        x2_a = x1_a  
        x1_b =(-2*c)/b #method b
        x2_b = x1_b  
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x1_a,"\n","x2_a=",x2_a,"\n Using method (b) the roots are the following: \n","x1_b=",x1_b,"\n","x2_b=",x2_b)
        return (x1_a,x2_a,x1_b,x2_b)
    elif d>0:
        print("The equation has real roots ")
        x1_a=(-b+sqrt(d))/(2*a) 
        x2_a=(-b-sqrt(d))/(2*a)
        x1_b=(-2*c)/(b+sqrt(d))
        x2_b=(-2*c)/(b-sqrt(d))        
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x1_a,"\n","x2_a=",x2_a,"\n Using method (b) the roots are the following: \n","x1_b=",x1_b,"\n","x2_b=",x2_b)
        return (x1_a,x2_a,x1_b,x2_b)
    else:
        print("The equation has complex roots ")
        x1_a=(-b+cm.sqrt(d))/(2*a)  
        x2_a=(-b-cm.sqrt(d))/(2*a) 
        x1_b=(-2*c)/(b+cm.sqrt(d))
        x2_b=(-2*c)/(b-cm.sqrt(d))
        print(" \n Using method (a) the roots are the following: \n","x1_a=",x1_a,"\n","x2_a=",x2_a,"\n Using method (b) the roots are the following: \n","x1_b=",x1_b,"\n","x2_b=",x2_b) 
        return (x1_a,x2_a,x1_b,x2_b)


a = 0.001 ; b = 1000 ; c = 0.001
x1_a,x2_a,x1_b,x2_b= quadsolve(a,b,c)