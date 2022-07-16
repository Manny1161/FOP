#
# conversions.py - module with functions to convert between units
# fahr2cel : Convert from Fahrenheit to Celcius
#

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celcius.
    Argument :
    fahr - the temperature in Fahrenheit
    """
    celcius = (fahr - 32) * (5/9)
    return celcius

def cel2fahr(cel):
    """Convert from Celcius to Fahrenheit.
    Argument : 
    cel - the temperature in Celcius
    """
    fahr = (cel * (9/5)) + 32
    return fahr

def kel2fahr(kel):
    """Convert from Celcius to Fahrenheit.
    Argument :
    cel - the temperature in Celcius
    """
    fahr = (kel -273.15) * (9/5) + 32
    return fahr

def kel2cel(kel):
    """Convert from Celcius to Fahrenheit.
    Argument :
    cel - the temperature in Celcius
    """
    cel = (kel - 273.15)
    return cel

def fahr2kel(fahr):
    """Convert from Celcius to Fahrenheit.
    Argument :
    cel - the temperature in Celcius
    """
    kel = (fahr -32) * (5/9) + 273.15
    return kel

def cel2kel(cel):
    """Convert from Celcius to Fahrenheit.
    Argument :
    cel - the temperature in Celcius
    """
    kel = (cel + 273.15)
    return kel
