import csv
import numpy as np
import pylab as plt
from scipy.stats import linregress

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
	delays_60.append(float(row[8]))

num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)
delays_15 = np.array(delays_15,dtype=float)
delays_30 = np.array(delays_30,dtype=float)
delays_60 = np.array(delays_60,dtype=float)


fig = plt.figure(1)
ax = fig.add_subplot(111)

x = np.array(range(len(delays)),dtype=int)

slope, intercept, r_value, p_value, std_err = linregress(x,delays)
print slope*12

ma = moving_average(delays,12)
ax.plot(x,ma,color='blue',linewidth=8)
ax.plot(x,delays,color='blue',alpha=.5)
ax.plot(x,slope*x + intercept)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_15)
print slope * 12

ma = moving_average(delays_15,12)
ax.plot(x,ma,color='green',linewidth=8)
ax.plot(x,delays_15,color='green',alpha=.5)
ax.plot(x,x*slope + intercept,color='green',alpha=.5)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_30)
print slope * 12

ma = moving_average(delays_30,12)
ax.plot(x,ma,color='cyan',linewidth=8)
ax.plot(x,delays_30,color='cyan',alpha=.5)
ax.plot(x,x*slope + intercept,color='green',alpha=.5)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_60)
print slope * 12

ma = moving_average(delays_60,12)
ax.plot(x,ma,color='magenta',linewidth=8)
ax.plot(x,delays_60,color='magenta',alpha=.5)
ax.plot(x,x*slope + intercept,color='green',alpha=.5)

plt.show()




