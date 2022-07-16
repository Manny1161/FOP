#
# Name : Emmanuel Kapela
# ID   : 20173115
#
# heat.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

size = 10 

hlist = []
with open('heatsource.csv') as f:
    for line in f:
        line_s = line.strip()
        ints = [int(x) for x in line_s.split(',')]
        hlist.append(ints)
    f.close()

h = np.array(hlist, dtype=int)
b = h.copy


def calcheat(r,c):
    next[r,c] = 0.1 * (curr[r-1:r+2, c-1:c+2].sum() + curr[r,c])
    return(next[r,c])

curr = np.zeros((size,size)) 
print(curr)    
for i in range(size): 
    curr[:,0] = 10 

next = np.zeros((size,size))

for timestep in range(100):
    for r in range(1, size-1): 
        for c in range (1, size- 1 ): 
            next[r,c] = calcheat(r,c)

    for r in range(size):
        for c in range(size):
            if h[r,c]>next[r,c]:
                next[r,c] = h[r,c]
    b = next.copy()

    for i in range(size): 
        next[:,0] = 10 

    print("Time step: ", timestep) 
    print(next)    
    curr = next.copy() 

plt.imshow(curr, cmap=plt.cm.hot) 
plt.show() 
