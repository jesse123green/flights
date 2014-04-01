import csv
import numpy as np
import pylab as plt



# f_thanks = open('analysis_data/holiday_delays_thanks.csv','r')
f_thanks = open('analysis_data/holiday_delays_mon_10.csv','r')
f = open('analysis_data/timeofday.csv','r')

thanks_data = csv.reader(f_thanks)
thanks_data.next()

csv_data = csv.reader(f)
csv_data.next()

delays = []
delays_60 = []
num_flights = []

delays_thanks = []
num_flights_thanks = []


for row in csv_data:
	num_flights.append(row[2])
	delays.append(row[8])
	delays_60.append(row[6])

for row in thanks_data:
	num_flights_thanks.append(row[2])
	delays_thanks.append(row[8])

num_flights = np.array(num_flights,dtype=int)/52.
num_flights_thanks = np.array(num_flights_thanks,dtype=int)/68. #10 for thanksgiving, 68 for mondays

# print delays
delays = np.array(delays,dtype=float)
delays_60 = np.array(delays_60,dtype=float)
delays_thanks = np.array(delays_thanks,dtype=float)

delays = np.roll(delays,3*24,axis=0)
num_flights = np.roll(num_flights,3*24,axis=0)

fig = plt.figure()

print len(delays_thanks),len(delays)

for k in np.array(range(7))*24:
	daymax = np.max(delays[k+5:k+24])
	plt.plot([k,k+24],[daymax,daymax],color='blue')

plt.stem(range(len(delays)),delays_thanks)

for k in range(7):
	print np.sum(num_flights[k*24:k*24+24])
	print np.sum(num_flights_thanks[k*24:k*24+24])
	print '-----------'
	plt.plot(k*24+12,-.025,'o',markersize=np.sum(num_flights[k*24:k*24+24])/20000.*100,color='blue')
	plt.plot(k*24+12,-.025,'o',markersize=np.sum(num_flights_thanks[k*24:k*24+24])/20000.*100,color='green',alpha=.5)

plt.xlim((0,24*7))
plt.ylim((-.05,.15))
# plt.plot(range(len(delays)),delays,color='blue')
# markerline, stemlines, baseline = plt.stem(range(len(delays)),delays_60)
# plt.setp(markerline, 'markerfacecolor', 'g')
plt.show()