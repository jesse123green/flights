import csv
import numpy as np
import pylab as plt



# f_thanks = open('analysis_data/holiday_delays/holiday_delays_thanks.csv','r')
# f_thanks = open('analysis_data/holiday_delays/holiday_delays_mon_10.csv','r')
f_thanks = open('analysis_data/holiday_delays/memorial_delays_10.csv','r')
f = open('analysis_data/tod/timeofday_all.csv','r')

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

num_flights = np.array(num_flights,dtype=int)/52./10.
num_flights_thanks = np.array(num_flights_thanks,dtype=int)/10. #10 for thanksgiving, 64 for mondays

# print delays
delays = np.array(delays,dtype=float)
delays_60 = np.array(delays_60,dtype=float)
delays_thanks = np.array(delays_thanks,dtype=float)


fig = plt.figure()
print 'Max delay:',np.max(delays_thanks)
print len(delays_thanks),len(delays)

## only roll if memorial day
# delays = np.roll(delays,4*24,axis=0)
# num_flights = np.roll(num_flights,4*24,axis=0)



# markerline, stemlines, baseline = plt.stem(range(len(delays)),delays_thanks)
# plt.setp(markerline, 'markerfacecolor', '#297538')
# plt.setp(stemlines, 'color','#297538')

markerline, stemlines, baseline = plt.stem(range(len(delays)),delays)


for k in np.array(range(7))*24:
	daymax = np.max(delays[k+5:k+24])
	plt.plot([k,k+24],[daymax,daymax],color='blue')


for k in range(7):

	# if np.sum(num_flights_thanks[k*24:k*24+24]) >= np.sum(num_flights[k*24:k*24+24]):
	# 	plt.annotate('+%.1f%%'%((np.sum(num_flights_thanks[k*24:k*24+24])/np.sum(num_flights[k*24:k*24+24])-1)*100.),xycoords='data',xy=(k*24+12,-.025),verticalalignment='center',horizontalalignment='center')
	# else:
	# 	plt.annotate('-%.1f%%'%((1-np.sum(num_flights_thanks[k*24:k*24+24])/np.sum(num_flights[k*24:k*24+24]))*100.),xycoords='data',xy=(k*24+12,-.025),verticalalignment='center',horizontalalignment='center')

	plt.annotate('%.1fk'%(np.sum(num_flights[k*24:k*24+24])/1000.),xycoords='data',xy=(k*24+12,-.025),verticalalignment='center',horizontalalignment='center')	

	print np.sum(num_flights[k*24:k*24+24])
	print np.sum(num_flights_thanks[k*24:k*24+24])
	print '-----------'
	plt.plot(k*24+12,-.025,'o',markersize=np.sum(num_flights[k*24:k*24+24])/20000.*100,color='blue')
	# plt.plot(k*24+12,-.025,'o',markersize=np.sum(num_flights_thanks[k*24:k*24+24])/20000.*100,color='#297538',alpha=.7)

ax = plt.gca()
ax.set_ylim((-.05,.2))
ax2 = ax.twinx()
plt.xticks(np.arange(12,24*7,12))
ax.set_ylabel('Percent Delayed for 60+ Minutes')
ax.set_yticks([0,.05,.1,.15,.2])
ax.yaxis.set_label_coords(-.05, .6)

ax2.set_yticks([])
ax2.set_ylabel('Number of \n   Flights')
ax2.yaxis.set_label_coords(-.03, .1)

ax.set_xticklabels(['Monday','','Tuesday','','Wednesday','','Thursday','','Friday','','Saturday','','Sunday'])
# ax.set_xticklabels(['Monday','','Tuesday','','Wednesday','','Thanksgiving','','Friday','','Saturday','','Sunday'])
# ax.set_xticklabels(['Thursday','','Friday','','Saturday','','Sunday','','Memorial Day','','Tuesday','','Wednesday'])
plt.xlim((0,24*7))
# plt.plot(range(len(delays)),delays,color='blue')
# markerline, stemlines, baseline = plt.stem(range(len(delays)),delays_60)
# plt.setp(markerline, 'markerfacecolor', 'g')
plt.show()