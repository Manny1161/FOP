#
#Student Name: Emmanuel Kapela
#Student ID: 20173115
#
#test1.py - create a string and print it

funstring = "Fundamentals of Programming (Welcome to Python-World!)"
print (funstring)

num = input("enter a number: ")
num = int(num)

index = 0

while index < num:
    print ("string = ", funstring, "index = ", index)
    index = index + 1
    if num % 2 == 1:
        print(funstring.lower()[::+3])
    else:
        print("reversed string =",funstring.upper()[::-2])
    

