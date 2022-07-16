#
# numbersarray.py: Read ten numbers give sum, min, max & mean
#
import numpy as np
import matplotlib.pyplot as plt

numArray = np.zeros(10) #--> creates an empty 10 element array

print('Enter ten numbers...')

for i in range(len(numArray)):
    print('Enter a number (', i, ')...')
    numArray[i] = int(input())
print('Total is', numArray.sum(), ' Min is', numArray.min(), 'Max is', numArray.max(), 'Average is', numArray.mean())

plt.title("Number Array")
plt.plot(numArray)
plt.show()
