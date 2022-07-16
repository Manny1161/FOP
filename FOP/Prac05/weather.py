import matplotlib.pyplot as plt

with open("marchweather.csv", 'r') as f:
    for line in f:
        print(line, end='')

f.close()

mins= line.split(',')
maxs= line.split(',')
dates=range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()
