import matplotlib.pyplot as plt
import numpy as np

data = [ float(line) for line in open('data.txt', 'r') ]

columnsCount = int(len(data) ** 0.5)
columnWidth = (data[-1] - data[0]) / columnsCount

columns = [0] * columnsCount
times = [ data[0] + (i + 0.5) * columnWidth for i in range(columnsCount) ]

idx = 0
for i in range(columnsCount):
	time = data[0] + columnWidth * (i + 1)
	while idx < len(data) and data[idx] < time:
		columns[i] += 1
		idx += 1
	columns[i] /= len(data) * columnWidth

average = np.average(data)
stdDeviation = np.std(data)

rhoMax = 1 / (stdDeviation * 2.5)

xs = np.linspace(data[0], data[-1], 50)
ys = rhoMax * 2.71 ** (((xs - average) ** 2.0) / (-2.0 * stdDeviation ** 2.0))

plt.plot(xs, ys, '-r')
plt.bar(times, columns, width=columnWidth, alpha=0.5)
plt.show()
