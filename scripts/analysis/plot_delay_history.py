import csv
import numpy as np
import pylab as plt

def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

# f = open('analysis_data/holiday_delays_thanks.csv','r')
f = open('analysis_data/flight_history.csv','r')
csv_data = csv.reader(f)
csv_data.next()

delays = []
delays_15 = []
delays_30 = []
delays_60 = []
num_flights = []

for row in csv_data:
	num_flights.append(row[2])
	# delays.append(float(row[5])*int(row[2]))
	delays.append(float(row[5]))
	delays_15.append(float(row[6]))
	delays_30.append(float(row[7]))
	delays_60.append(row[8])

num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)
delays_15 = np.array(delays_15,dtype=float)
delays_30 = np.array(delays_30,dtype=float)
delays_60 = np.array(delays_60,dtype=float)


fig = plt.figure(1)
ax = fig.add_subplot(111)
# ax.bar(range(len(delays)), delays, 1, color='#deb0b0',alpha=.5)
ma = moving_average(delays,12)
ax.plot(range(len(ma)),ma,color='blue',linewidth=8)
ax.plot(range(len(delays)),delays,color='blue',alpha=.5)

ma = moving_average(delays_15,12)
ax.plot(range(len(ma)),ma,color='green',linewidth=8)
ax.plot(range(len(delays)),delays_15,color='green',alpha=.5)

ma = moving_average(delays_30,12)
ax.plot(range(len(ma)),ma,color='cyan',linewidth=8)
ax.plot(range(len(delays)),delays_30,color='cyan',alpha=.5)

ma = moving_average(delays_60,12)
ax.plot(range(len(ma)),ma,color='magenta',linewidth=8)
ax.plot(range(len(delays)),delays_60,color='magenta',alpha=.5)


# print len(delays),len(ma)
# ax2 = ax.twinx()
# # ax2.bar(range(len(delays)), delays_60, 1, color='#b0c4de',alpha=.5)
# ma2 = moving_average(num_flights,12)
# ax2.plot(range(len(ma2)),ma2,color='blue',linewidth=8)
# ax2.plot(range(len(num_flights)),num_flights,color='blue',alpha=.5)
# ax2.set_ylim((0,.12))

# ax.yaxis.set_ticks_position("right")
# ax2.yaxis.set_ticks_position("left")

plt.show()