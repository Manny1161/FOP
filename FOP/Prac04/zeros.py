#
# zeros.py - creating and resizing an array
#
import numpy as np

print ("\nZEROS ARRAY\n")
zeroarray = np.zeros((2,2,0))

print('Zero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((3,9))
print('\nZero array size: ', np.size(zeroarray))
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)
