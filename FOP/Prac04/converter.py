from conversions import *

print("MAIN MENU FOR CONVERSIONS")

print("[0] CELCIUS TO FAHRENHEIT")
print("[1] FAHRENHEIT TO CELCIUS")
print("[2] CELCIUS TO KELVIN")
print("[3] KELVIN TO CELCIUS")
print("[4] FAHRENHEIT TO KELVIN")
print("[5] KELVIN TO FAHRENHEIT")
print("[6] EXIT")
    
uConv = int(input("use integers to select the conversion you want: "))
while uConv != 6:

    if uConv == int(0):
        c2f = int(input("Enter Celcius temperature to convert to Fahrenheit: "))
        cel = cel2fahr(c2f)
        print(cel)
    elif uConv == int(1):
        f2c = int(input("Enter Fahrenheit temperature to convert to Celcius: "))
        celcius = fahr2cel(f2c)
        print(celcius)
    elif uConv == int(2):
        c2k = int(input("Enter Celcius temperature to convert to Kelvin: "))
        kel = cel2kel(c2k)
        print(kel)
    elif uConv == int(3):
        k2c = int(input("Enter Celcius temperature to convert to Kelvin: "))
        cel = kel2cel(k2c)
        print(cel)
    elif uConv == int(4):
        f2k = int(input("Enter Celcius temperature to convert to Kelvin: "))
        kel = fahr2kel(f2k)
        print(kel)
    elif uConv == int(5):
        k2f = int(input("Enter Celcius temperature to convert to Kelvin: "))
        fahr = kel2fahr(k2f)
        print(fahr)
    else:
        uConv = int(input("ERROR: Re-enter an integer between 0 and 5!: "))
    print("[0] CELCIUS TO FAHRENHEIT")
    print("[1] FAHRENHEIT TO CELCIUS")
    print("[2] CELCIUS TO KELVIN")
    print("[3] KELVIN TO CELCIUS")
    print("[4] FAHRENHEIT TO KELVIN")
    print("[5] KELVIN TO FAHRENHEIT")
    print("[6] EXIT")
    uConv = int(input("use integers to select the conversion you want: "))
    

    

