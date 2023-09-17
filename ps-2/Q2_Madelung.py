from numpy import*
def Madelung(L):
    m1 = 0
    for i in range(1,L+1):
        m1 += ((-1)**(i+1))/sqrt(i**2)
    m2 = 0
    for i in range(1,L+1):
        for j in range(1,L+1):
            m2 += ((-1)**(i+j+1))/sqrt(i**2+j**2)
    m3 = 0
    for i in range(1,L+1):
        for j in range(1,L+1):
            for k in range(1,L+1):
                m3+=((-1)**(i+j+k+1))/sqrt(i**2+j**2+k**2)
    return 6*m1 + 12*m2 + 8*m3
l=100
print("Madelung Constant is", Madelung(l))