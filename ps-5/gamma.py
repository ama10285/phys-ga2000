from pylab import*

#section a
def func(a,x):
    return exp(((a-1)*log(x))-x)

x=linspace(0.001,5,100)
plot(x,func(2,x),'b',label='a=2')
plot(x,func(3,x),'g',label='a=3')
plot(x,func(4,x),'r',label='a=4')
legend(loc=2)
title('Integrand of the Gamma Function for Different Values of n')
xlabel('x')
ylabel('Integrand')
show()

# section e + f
def gamma(a):
    z=linspace(0.001,0.999,1000)
    x=(a-1)*z/(1-z)
    integrand=exp(((a-1)*log(x))-x)
    integral=0.0
    for i in range(len(x)-1):
        integral=integral+0.5*(integrand[i]+integrand[i+1])*(x[i+1]-x[i])
    return integral

print('gamma(3/2) = ',gamma(3/2))
print('gamma(3) = ',gamma(3))
print('gamma(6) = ',gamma(6))
print('gamma(10) = ',gamma(10))

