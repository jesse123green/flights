import csv
import numpy as np
import pylab as plt



f = open('analysis_data/holiday_delays_thanks.csv','r')
csv_data = csv.reader(f)
csv_data.next()

delays = []
delays_60 = []
num_flights = []

for row in csv_data:
	num_flights.append(row[2])
	delays.append(row[6])
	delays_60.append(row[8])

print delays
delays = np.array(delays,dtype=float)
delays_60 = np.array(delays_60,dtype=float)

print delays_60

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.bar(range(len(delays)), delays, 1, color='#deb0b0',alpha=.5)
ax.plot(range(len(delays)),num_flights)

ax2 = ax.twinx()
ax2.bar(range(len(delays)), delays_60, 1, color='#b0c4de',alpha=.5)
ax2.set_ylim((0,.12))

ax.yaxis.set_ticks_position("right")
ax2.yaxis.set_ticks_position("left")

plt.show()