#
# growthSubplot - plot the growth of arrays
#

import matplotlib.pyplot as plt
import numpy as np

print("\nSIMULATION - Unconstrained Growth\n")
length = 100
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ", num_iter)
print("Growth step (growth rate per time step): ", growth_step)

print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
times = [0]
pops = [100]

for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    popArr = np.array(population)
    population = popArr
    time = i * time_step
    timeArr = np.array(time)
    time = timeArr
    times.append(timeArr)
    pops.append(popArr)
    print("Time: ", timeArr, " \tGrowth: ", growth,
        " \tPopulation: ", popArr)
print("\nPROCESSING COMPLETE.\n")

plt.figure(1)
plt.subplot(211)
plt.plot(times, pops, '--')
plt.title('population growth')
plt.ylabel('population')

plt.subplot(212)
plt.plot(times, pops, 'ro')
plt.ylabel('population')
plt.xlabel('time')
plt.show

plt.title("Prac 3.1: Unconstrained Growth")
plt.plot(times, pops, 'r')
plt.show()