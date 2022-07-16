import random
trials = input("How many tosses would you like?...")

coin = ['heads','tails']
heads = 0
tails = 0

print('\nCOIN TOSS\n')

for index in range(int(trials)):
    if random.choice (coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')
