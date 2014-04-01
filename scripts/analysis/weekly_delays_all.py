import csv, sys
import numpy as np
import pylab as plt
from scipy.stats import pearsonr
def moving_average(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')



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
	print np.min(delays),np.max(delays)
	num_flights_weekday = []
	delays_weekday = []


	# print num_flights

	for day in np.unique(weekdays):
		dayI = (weekdays == day)

		num_flights_weekday.append(np.sum(num_flights[dayI]))
		delays_weekday.append(np.average(delays[dayI],weights=num_flights[dayI]))


	num_flights_weekday = 1.0*np.array(num_flights_weekday,dtype=int)/np.max(num_flights_weekday)

	# print delays_weekday

	fig = plt.figure(1)

	for k in range(len(delays_weekday)):
		# plt.plot(k+.5,num_flights_weekday[k]/5.,'o',markersize=delays_weekday[k]*100,color='green',alpha=.7)
		# plt.plot(k+.5,delays_weekday[k],'o',markersize=num_flights_weekday[k]*10,color='green',alpha=.7)
		plt.plot(k+.5,thisday,'o',markersize=np.ceil(num_flights_weekday[k]*40),color='green',alpha=delays_weekday[k]*4)
plt.xticks(range(24))
plt.yticks(np.array(range(7)) + .5)
plt.grid()
plt.xlim((0,24))
plt.ylim((-.5,6.5))
plt.show()
sys.exit()

f = open('analysis_data/timeofday.csv','r')
csv_data = csv.reader(f)
csv_data.next()

delays = []
num_flights = []
weekdays = []

for row in csv_data:
	print row
	if int(row[0]) in [5]:
		weekdays.append(row[1])
		num_flights.append(int(row[2]))
		delays.append(float(row[d]))



num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)
weekdays = np.array(weekdays)

num_flights_weekday = []
delays_weekday = []


# print num_flights

for day in np.unique(weekdays):
	dayI = (weekdays == day)
	
	num_flights_weekday.append(np.sum(num_flights[dayI]))
	delays_weekday.append(np.average(delays[dayI],weights=num_flights[dayI]))


num_flights_weekday = 1.0*np.array(num_flights_weekday,dtype=int)/np.max(num_flights_weekday)

# fig = plt.figure(1)

for k in range(len(delays_weekday)):
	# plt.plot(k+.5,num_flights_weekday[k],'o',markersize=delays_weekday[k]*100,color='red',alpha=.7)
	plt.plot(k+.5,delays_weekday[k],'o',markersize=num_flights_weekday[k]*100,color='red',alpha=.7)
f = open('analysis_data/timeofday.csv','r')
csv_data = csv.reader(f)
csv_data.next()

delays = []
num_flights = []
weekdays = []

for row in csv_data:
	print row
	if int(row[0]) in [6]:
		weekdays.append(row[1])
		num_flights.append(int(row[2]))
		delays.append(float(row[d]))



num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)
weekdays = np.array(weekdays)

num_flights_weekday = []
delays_weekday = []


# print num_flights

for day in np.unique(weekdays):
	dayI = (weekdays == day)
	
	num_flights_weekday.append(np.sum(num_flights[dayI]))
	delays_weekday.append(np.average(delays[dayI],weights=num_flights[dayI]))


num_flights_weekday = 1.0*np.array(num_flights_weekday,dtype=int)/np.max(num_flights_weekday)

# fig = plt.figure(1)

for k in range(len(delays_weekday)):
	# plt.plot(k+.5,num_flights_weekday[k],'o',markersize=delays_weekday[k]*100,color='blue',alpha=.7)
	plt.plot(k+.5,delays_weekday[k],'o',markersize=num_flights_weekday[k]*100,color='blue',alpha=.7)


plt.xlim((0,24))
plt.show()