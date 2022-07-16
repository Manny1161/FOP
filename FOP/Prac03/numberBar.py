#
# numberBar.py: Read ten numbers give sum, min, max & mean, plot them in a bar
#
import numpy as np
import matplotlib.pyplot as plt

numArray = np.zeros(10) #--> creates an empty 10 element array

print('Enter ten numbers...')

for i in range(len(numArray)):
    print('Enter a number (', i, ')...')
    numArray[i] = int(input())
print('Total is', numArray.sum(), ' Min is', numArray.min(), 'Max is', numArray.max(), 'Average is', numArray.mean())

plt.title("Number bar chart")
plt.xlabel('index')
plt.ylabel('number')
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numArray, 0.9, color='purple')
plt.show()
