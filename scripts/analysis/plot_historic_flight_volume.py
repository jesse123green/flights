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



### yearly

# delays = []
# num_flights = []
# years = []

# for row in csv_data:
# 	years.append(row[0])
# 	num_flights.append(row[2])
# 	# delays.append(float(row[5])*int(row[2]))
# 	delays.append(float(row[5]))

# years = np.array(years,dtype=int)
# num_flights = np.array(num_flights,dtype=int)
# delays = np.array(delays,dtype=float)

# num_flights_year = []
# delays_year = []
# for year in range(1988,2014):
# 	yearI = (years == year)
# 	print num_flights[yearI]
# 	print delays[yearI]
# 	print '-'*20
# 	num_flights_year.append(np.sum(num_flights[yearI]))
# 	delays_year.append(np.average(delays[yearI],weights=num_flights[yearI]))
# print num_flights_year
# print delays_year

# fig = plt.figure(1)
# ax = fig.add_subplot(111)
# # ax.bar(range(len(delays_year)), num_flights_year, .85, color='#b0c4de')

# ax2 = ax.twinx()
# # # ax2.bar(range(len(delays)), delays_60, 1, color='#b0c4de',alpha=.5)
# # ma2 = moving_average(num_flights,12)
# # ax2.plot(range(len(delays_year)),delays_year, color='#deb0b0',linewidth=8)
# ax2.plot(range(len(num_flights)),moving_average(num_flights,12), color='#deb0b0',linewidth=8)
# ax2.plot(range(len(num_flights)),num_flights,color='blue',alpha=.5)
# ax2.set_ylim((0,650000))

# # ax.yaxis.set_ticks_position("right")
# # ax2.yaxis.set_ticks_position("left")

# plt.show()


### Monthly

delays = []
num_flights = []
years = []

for row in csv_data:
	years.append(row[1])
	num_flights.append(row[2])
	# delays.append(float(row[5])*int(row[2]))
	delays.append(float(row[5]))

years = np.array(years,dtype=int)
num_flights = np.array(num_flights,dtype=int)
delays = np.array(delays,dtype=float)

num_flights_year = []
delays_year = []
for year in range(1,13):
	yearI = (years == year)
	# print num_flights[yearI]
	# print delays[yearI]
	# print '-'*20
	num_flights_year.append(np.sum(num_flights[yearI])/26.)
	delays_year.append(np.average(delays[yearI],weights=num_flights[yearI]))

print num_flights_year

fig = plt.figure(1)
ax = fig.add_subplot(111)
# ax.bar(range(len(delays_year)), num_flights_year, .85, color='#b0c4de')

ax2 = ax.twinx()
# # ax2.bar(range(len(delays)), delays_60, 1, color='#b0c4de',alpha=.5)
# ma2 = moving_average(num_flights,12)
# ax2.plot(range(len(delays_year)),delays_year, color='#deb0b0',linewidth=8)
# ax2.plot(range(len(num_flights_year)),moving_average(num_flights_year,12), color='#deb0b0',linewidth=8)
ax2.plot(range(len(num_flights_year)),num_flights_year,color='blue',alpha=.5)
ax2.set_ylim((0,650000))

# ax.yaxis.set_ticks_position("right")
# ax2.yaxis.set_ticks_position("left")

plt.show()