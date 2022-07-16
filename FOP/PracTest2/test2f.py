#
# Student Name: Emmanuel Kapela 
# Student ID  : 20173115
#
# test2f.py: Simulate spread of disease through a population 
#            using SIR model 
# 
# Based on SIR model:
#    Shiflet&Shiflet Module 4.3 Modeling the Spread of SARS
#    and https://www.youtube.com/watch?v=k6nLfCbAzgo
#

import matplotlib.pyplot as plt
import numpy as np

Scur = 762   # number of people susceptible
Icur = 1     # number of people infected
Rcur = 0     # number of people recovered

trans_const = 0.00218   # infectiousness of disease r = kb/N
recov_rate = 0.5        # recovery rate a = 1/(# days infected)
simlength = 20          # number of days in simulation

resultarray = np.zeros((simlength,3)) # 2D array of floats
resultarray[0,:] = Scur, Icur, Rcur     # record initial values

for i in range(1, simlength):
    new_infected = trans_const * Scur * Icur   # = rSI
    new_recovered = recov_rate * Icur          # = aI

    Scur = Scur - new_infected
    Icur = Icur + new_infected - new_recovered
    Rcur = Rcur + new_recovered

    resultarray[i,:] = Scur, Icur, Rcur
 
print("\tScur   \t\tIcur    \tRcur")
print(resultarray)

plt.plot(resultarray)
plt.plot(resultarray[:,0], 'g')
plt.plot(resultarray[:,1], 'ro')
plt.plot(resultarray[:,2], 'bD')
plt.title('SIR Model parameters r: ' + str(trans_const) + ' a: ' + str(recov_rate))
plt.xlabel('# Days')
plt.ylabel('# People')

plt.show()

plt.figure(1)
plt.subplot(221)
plt.plot(resultarray[:,0], 'g')
plt.title('Susceptible')
plt.suptitle('SIR Model parameters r: ' + str(trans_const) + ' a: ' + str(recov_rate))

plt.subplot(222)
plt.title('Combined')
plt.plot(resultarray)

plt.subplot(223)
plt.plot(resultarray[:,1], 'ro')
plt.title('Infected')

plt.subplot(224)
plt.plot(resultarray[:,2], 'bD')
plt.title('Recovered')

plt.show()
