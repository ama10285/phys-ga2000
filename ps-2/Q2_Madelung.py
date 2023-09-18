from numpy import*
import timeit

def Madelung_1(L):
    m1 = 0
    for i in range(1, L + 1):
        m1 += ((-1)**(i + 1)) / sqrt(i**2)
    m2 = 0
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            m2 += ((-1)**(i + j + 1)) / sqrt(i**2 + j**2)
    m3 = 0
    for i in range(1, L + 1):
        for j in range(1, L + 1):
            for k in range(1, L + 1):
                m3 += ((-1)**(i + j + k + 1)) / sqrt(i**2 + j**2 + k**2)
    return 6*m1 + 12*m2 + 8*m3


def Madelung_2(L):
    i, j, k = meshgrid(arange(-L, L + 1), arange(-L, L + 1), arange(-L, L + 1))
    i[L, L, L] = 1
    j[L, L, L] = 1
    k[L, L, L] = 1
    m = (sum((-1.0)**((i + j + k)) / sqrt(i**2 + j**2 + k**2)) + 1 / sqrt(3))*(-1.0)
    return m

l = 100
print("Madelung Constant using Method 1 is", Madelung_1(l))
print("Madelung Constant using Method 2 is", Madelung_2(l))

#Use %timeit to determine which is faster
time_method1 = timeit.timeit(lambda:Madelung_1(l),number=5)
print("Method 1 execution time:", time_method1)
time_method2 = timeit.timeit(lambda: Madelung_2(l),number=5)
print("Method 2 execution time:", time_method2)
