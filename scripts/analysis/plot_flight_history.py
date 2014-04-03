import csv
import numpy as np
import pylab as plt
from scipy.stats import pearsonr, linregress

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
	# print row
	num_flights.append(row[2])
	# delays.append(float(row[5])*int(row[2]))
	delays.append(float(row[5]))


num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)
slope, intercept, r_value, p_value, std_err = linregress(range(len(delays)),delays)

print slope*12

# print pearsonr(delays,num_flights)

window = 7 # even please

i = np.array(range(int(np.ceil(window/2.)),int(len(delays)-np.ceil(window/2.))))

fig = plt.figure(1)
plt.xlim((0,315))
ax = fig.add_subplot(111)
ax.set_xticks([3,3+5*12,3+10*12,3+15*12,3+20*12,3+25*12])
ax.set_xticklabels(['1988','1993','1998','2003','2008','2013'])
# ax.bar(range(len(delays)), delays, 1, color='#deb0b0',alpha=.5)
ma = moving_average(delays,window)

ax.plot(i,ma[i],color='blue',linewidth=2,label='Percent Delayed')
ax.plot(range(len(delays)),delays,color='blue',alpha=.5)
ax.plot(range(len(delays)),slope*np.array(range(len(delays)))+intercept,linestyle='-',color='#404040',linewidth=2)
ax.set_ylim((0,1))
ax.set_yticks([.2,.4,.6,.8,1])
ax.set_ylabel('Number of Flights in Thousands')
ax.yaxis.set_label_coords(-.05, .5)
ax.set_xlabel('Year')


ax2 = ax.twinx()
# # ax2.bar(range(len(delays)), delays_60, 1, color='#b0c4de',alpha=.5)
ma2 = moving_average(num_flights,window)
ax2.plot(i,ma2[i],color='green',linewidth=2,label='Flight Volume')
ax2.plot(range(len(num_flights)),num_flights,color='green',alpha=.5)
ax2.set_ylim((0,650000))
ax2.set_ylabel('Percentage of Flights Delayed')
ax2.yaxis.set_label_coords(1.05, .5)

ax.yaxis.set_ticks_position("right")
ax2.yaxis.set_ticks_position("left")

ax2.set_yticklabels(['','100','200','300','400','500','600'])

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.show()