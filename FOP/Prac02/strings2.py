instring = input('Enter a string... ')
# *** add upper and duplicating code here
print(instring.upper())
print(instring + instring) 
# reversing with a while loop

print('Reversed string is : ', end='')
index = 0
while index >= len(instring):
    print(instring[index]) +1
    index = index + 1

# reversing with a range loop

print('Reversed string is : ', end='')
for index in range(len(instring)):
    print(instring[index], end='')
print()

# reversing with slicing

print('Reversed string is :', instring[1::+2])
