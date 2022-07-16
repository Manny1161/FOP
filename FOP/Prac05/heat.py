#
# Name : Emmanuel Kapela
# ID   : 20173115
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

size = 10 

def calcheat(r,c):
    next[r,c] = 0.1 * (curr[r-1:r+2, c-1:c+2].sum() + curr[r,c])
    return(next[r,c])

curr = np.zeros((size,size)) 
print(curr)    
for i in range(size): 
    curr[i,0] = 10 

next = np.zeros((size,size))

for timestep in range(5): 
    for r in range(1, size-1): 
        for c in range (1, size- 1 ): 
            next[r,c] = calcheat(r,c) 

    for i in range(size): 
        next[i,0] = 10 

    print("Time step: ", timestep) 
    print(next)    
    curr = next.copy() 

plt.imshow(curr, cmap=plt.cm.hot) 
plt.show() 
