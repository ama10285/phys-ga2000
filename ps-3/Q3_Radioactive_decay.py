from pylab import*
import random 

N_Bi213 = 10000
N_Pb209 = 0
N_Tl209 = 0
N_Bi209 = 0

tau_route1 = [46 * 60, 3.3 * 60]  
tau_route2 = [2.2 * 60, 3.3 * 60]  

p_route1 = 1 - 2 ** (-1.0 / tau_route1[0])  
p_route2 = 1 - 2 ** (-1.0 / tau_route2[0])  

tmax = 25000
tpoints = arange(0.0, tmax, 1.0)  

Bi213_counts = []
Pb209_counts = []
Tl209_counts = []
Bi209_counts = []

for t in tpoints:
    Bi213_counts.append(N_Bi213)
    Pb209_counts.append(N_Pb209)
    Tl209_counts.append(N_Tl209)
    Bi209_counts.append(N_Bi209)

    decay_route1 = 0
    for i in range(N_Bi213):
        if random.random() < p_route1:
            decay_route1 += 1
    N_Bi213 -= decay_route1
    N_Pb209 += decay_route1

    decay_route2 = 0
    for i in range(N_Tl209):
        if random.random() < p_route2:
            decay_route2 += 1
    N_Tl209 -= decay_route2
    N_Pb209 += decay_route2

    decay_pb_to_bi = 0
    for i in range(N_Pb209):
        if random.random() < (1 - 2 ** (-1.0 / tau_route1[1])):
            decay_pb_to_bi += 1
    N_Pb209 -= decay_pb_to_bi
    N_Bi209 += decay_pb_to_bi

figure(figsize=(10, 6))
plot(tpoints, Bi213_counts, label="Bi-213")
plot(tpoints, Pb209_counts, label="Pb-209")
plot(tpoints, Tl209_counts, label="Tl-209")
plot(tpoints, Bi209_counts, label="Bi-209")
title("Radioactive Decay Simulation")
xlabel("Time (seconds)")
ylabel("Number of atoms")
legend()
grid()
show()



