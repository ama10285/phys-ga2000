from pylab import*
import random
import numpy as np 
r = 1.1  
T_half = 3.053  
num_atoms = 1000  
max_time = 10  

random_uniform = np.random.rand(num_atoms)
decay_times = -log(1 - random_uniform) / r
decay_times.sort()
time_points = linspace(0, max_time, 1000)

num_atoms_not_decayed = []
for t in time_points:
    count_undecayed = sum(decay_times > t)
    num_atoms_not_decayed.append(count_undecayed) 

plot(time_points, num_atoms_not_decayed)
xlabel("Time (mins)")
ylabel("Number of Atoms Not Decayed")
title("Decay of 208Tl Atoms")
grid()
show()