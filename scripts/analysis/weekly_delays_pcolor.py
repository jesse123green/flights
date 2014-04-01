import csv, sys
import numpy as np
import pylab as plt
from scipy.stats import pearsonr
def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')


all_delays = []

d = 7

for thisday in range(7):
	f = open('analysis_data/timeofday.csv','r')
	csv_data = csv.reader(f)
	csv_data.next()

	delays = []
	num_flights = []
	weekdays = []

	for row in csv_data:
		if int(row[0]) == thisday:
			weekdays.append(row[1])
			num_flights.append(int(row[2]))
			delays.append(float(row[d]))



	num_flights = np.array(num_flights,dtype=int)
	delays = np.array(delays,dtype=float)
	weekdays = np.array(weekdays)

	all_delays.append(delays)

all_delays = np.array(all_delays,dtype=float)

print np.min(np.min(all_delays)),np.max(np.max(all_delays))

# plt.xticks(range(24))
# plt.yticks(np.array(range(7)) + .5)
# plt.grid()
# plt.xlim((0,24))
# plt.ylim((-.5,6.5))
plt.pcolor(all_delays,cmap='Blues',vmin=0,vmax=np.max(np.max(all_delays)))
plt.show()
sys.exit()
