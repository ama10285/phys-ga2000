from pylab import *
import timeit
import numpy as np

matrix_sizes = []
explicit_method = []
dot_method = []
NN = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for N in NN:
    matrix_sizes.append(N)
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

def MM(A, B, N):
    C = zeros([N, N], float)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    return C 

def dt(A, B):
    C_dot = dot(A, B)
    return C_dot  

time_method1 = []
for N in NN:
    time_method1.append(timeit.timeit(lambda: MM(A, B, N), number=1))

time_method2 = []
for N in NN:
    time_method2.append(timeit.timeit(lambda: dt(A, B), number=1))

    
figure(figsize=(6, 5))
plot(matrix_sizes, time_method1 , label="Explicit Multiplication Method")
plot(matrix_sizes, time_method2, label="Dot Method")
xlabel("Matrix Size (N x N)")
ylabel("Execution Time (sec)")
title("Execution Time vs. Matrix Size")
grid()
legend()
show()
# Print the execution times
print("Execution Time (Explicit Multiplication Method) for N =", NN[0], ":", time_method1[0], "seconds")
print("Execution Time (dot Method) for N =", NN[0], ":", time_method2[0], "seconds")


print("Execution Time (Explicit Multiplication Method) for N =", NN[9], ":", time_method1[9], "seconds")
print("Execution Time (dot Method) for N =", NN[9], ":", time_method2[9], "seconds")