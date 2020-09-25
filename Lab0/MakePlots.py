import matplotlib.pyplot as plt

f = open('data.txt', 'r')

data = []
for line in f:
	data.append(float(line))

step = (data[-1] - data[0]) / len(data) ** 0.5

columns = []
times = []

idx = 0
time = data[idx]
while idx < len(data):
	columns.append(0)
	times.append(time + step * 0.5)
	time += step
	while idx < len(data) and data[idx] < time:
		columns[-1] += 1
		idx += 1
	columns[-1] /= len(data) * step


average = 0
for val in data:
	average += val
average /= len(data)

stdDeviation = 0
for val in data:
	stdDeviation += (val - 5.0) ** 2.0
controlSum = stdDeviation
stdDeviation /= len(data)
stdDeviation = stdDeviation ** 0.5

rhoMax = 1 / (stdDeviation * 2.5)

xs = []
ys = []

t = data[0]
while t < data[-1]:
	xs.append(t)
	ys.append(rhoMax * 2.71 ** (((t - average) ** 2.0) / (-2.0 * stdDeviation ** 2.0)))
	t += 0.025

sigma = 0
for val in data:
	sigma += (val - average) ** 2.0
sigma /= len(data) * (len(data) - 1)
sigma = sigma ** 0.5

studentFactor = step / sigma 

def calcSigma(num):
	cnt = 0
	for val in data:
		if (val > average - num * stdDeviation and val < average + num * stdDeviation):
		 	cnt += 1

	return cnt / len(data)

P = []
P.append(calcSigma(1))
P.append(calcSigma(2))
P.append(calcSigma(3))

print("Average: ", average)
print("Standart deviation: ", stdDeviation)
print("Control sum: ", controlSum)
print("Average sigma: ", sigma)
print("Rho max: ", rhoMax)
print("Student factor: ", studentFactor)
print("P's: ", *P)
print(*columns)

plt.plot(xs, ys, '-r')
plt.bar(times, columns, width=step, alpha=0.5)
plt.show()
