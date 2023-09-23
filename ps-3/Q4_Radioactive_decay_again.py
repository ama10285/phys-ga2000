from pylab import*
import random
import numpy as np 
r = 1.1  # Decay rate
T_half = 3.053  # Half-life of 208Tl in minutes
num_atoms = 1000  # Number of atoms to simulate
max_time = 10  # Adjust this value based on your needs

random_uniform = np.random.rand(num_atoms)
decay_times = -log(1 - random_uniform) / r
decay_times.sort()
time_points = linspace(0, max_time, 1000)

# compute atoms not decayed 
num_atoms_not_decayed = []
for t in time_points:
    count_undecayed = sum(decay_times > t)
    num_atoms_not_decayed.append(count_undecayed) 

plot(time_points, num_atoms_not_decayed)
xlabel("Time (mins)")
ylabel("Number of Atoms Not Decayed")
title("Decay of 208Tl Atoms")
show()