#!/usr/bin/env python
# coding: utf-8

# In[41]:


from pylab import*

def g(x,m,sd):  # normalized gaussian formula 
    return (1/(sd*(2*pi)**0.5))*exp(-(x-m)**2/(2*sd**2))

x = linspace(-10,10,1000) #data points 
m = 0   # mean
sd = 3  # standard deviation

plot(x,g(x,m,sd),label="Normalized Gaussian")
title("Gaussian Distribution Plot (Mean = 0, Standard Deviation = 3)")
xlabel(" X ")
ylabel(" Probability Density ")
legend()
grid()
savefig("gaussian.png")
show()

