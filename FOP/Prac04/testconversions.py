#
# testconversions.py - tests the functions in conversions.py
#

from conversions import *
print("\nTESTING CONVERSIONS\n")
testF = 100
testCel = 37.77
testK = 273.15
testC = fahr2cel(testF)
testFahr = cel2fahr(testC)
testKel = cel2kel(testK)
print("Fahrenheit is ", testF, " Celcius is ", testC)
print("Celcius is ", testCel, "Fahrenheit is ", testFahr)
print("Celcius is ", testCel, "Kelvin is", testKel)
print()
