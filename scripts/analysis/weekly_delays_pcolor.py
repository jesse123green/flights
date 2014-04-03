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
	f = open('analysis_data/tod/timeofday_all.csv','r')
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
all_delays = np.flipud(all_delays)
fig, ax = plt.subplots(figsize=(24,5.5))
# plt.xticks(range(24))
# plt.yticks(np.array(range(7)) + .5)
# plt.grid()
cax = ax.pcolor(all_delays,cmap='Blues',vmin=0,vmax=.22)
plt.xlim((0,24))
plt.xlabel('Departure Time')
ax.set_xticks([0,5,10,15,20])
ax.set_xticklabels(['00:00','05:00','10:00','15:00','20:00'])
ax.set_yticks(np.arange(.5,7.5,1))
ax.set_yticklabels(['Sun','Sat','Fri','Thu','Wed','Tue','Mon'])
cbar = fig.colorbar(cax, ticks=[0, .11, .22])
# cbar.ax.set_yticklabels(['< -1', '0', '> 1'])# vertically oriented colorbar
plt.savefig('plots/heatmap_all.png')
# plt.colorbar()
# plt.show()
sys.exit()


