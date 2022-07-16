import matplotlib.pyplot as plt

with open('marchweather2.csv', 'r') as f:
    read = f.readlines()

f.close()

mins = []
maxs = []
nines = []
threes = []
dates = range(1,32)

for line in read:
    splitline=line.split(',')
    mins.append(splitline[2])
    maxs.append(splitline[3])
    nines.append(splitline[10])
    threes.append(splitline[16])

file2 = open('marchout.csv', 'w')
for i in range(len(mins)):
    file2.write(mins[i]+ ',' + maxs[i] + ',' + nines[i] + ',' + threes[i] + '\n')
file2.close()


plt.plot(mins, maxs, nines, threes)
plt.show()
