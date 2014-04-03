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

window = 7

i = np.array(range(int(np.ceil(window/2.)),int(len(delays)-np.ceil(window/2.))))

fig = plt.figure(1)
ax = fig.add_subplot(111)

ax.set_ylim((0,.6))
ax.set_xticks([3,3+5*12,3+10*12,3+15*12,3+20*12,3+25*12])
ax.set_xticklabels(['1988','1993','1998','2003','2008','2013'])

ma0 = moving_average(delays,window)
ma15 = moving_average(delays_15,window)
ma30 = moving_average(delays_30,window)
ma60 = moving_average(delays_60,window)

x = np.array(range(len(delays)),dtype=int)
plt.xlim((i[0],i[-1]))
slope, intercept, r_value, p_value, std_err = linregress(x,delays)
print slope*12

ma = moving_average(delays,window)
ax.plot(i,ma[i],color='blue',linewidth=3,label='0+ mins')
ax.plot(x,delays,color='blue',alpha=.5)
ax.fill_between(i, ma15[i], ma0[i],color='blue',alpha=.65)
# ax.plot(x,slope*x + intercept)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_15)
print slope * 12

ma = moving_average(delays_15,window)
ax.plot(i,ma[i],color='green',linewidth=3,label='15+ mins')
ax.plot(x,delays_15,color='green',alpha=.5)
ax.fill_between(i, ma30[i], ma15[i],color='green',alpha=.65)
# ax.plot(x,x*slope + intercept,color='green',alpha=.5)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_30)
print slope * 12


ax.plot(i,ma30[i],color='#EA2E41',linewidth=3,label='30+ mins')
ax.plot(x,delays_30,color='#EA2E41',alpha=.5)
ax.fill_between(i, ma60[i], ma30[i],color='#EA2E41',alpha=.65)
# ax.plot(x,x*slope + intercept,color='#EA2E41',alpha=.5)

slope, intercept, r_value, p_value, std_err = linregress(x,delays_60)
print slope * 12

color = '#707070' 


ax.plot(i,ma60[i],color=color,linewidth=3,label='60+ mins')
ax.plot(x,delays_60,color=color,alpha=.5)
ax.fill_between(i, 0, ma60[i],color=color,alpha=.65)
# ax.plot(x,x*slope + intercept,color='green',alpha=.5)

ax.set_xlabel('Year')
ax.set_ylabel('Percent Delayed')

ax.legend(loc='upper right')

plt.show()




