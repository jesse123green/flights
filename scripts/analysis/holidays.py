import MySQLdb
import sys, csv
import time as time2
import numpy as np
from datetime import datetime, timedelta, date, time

def median(values,counts):
	total = np.sum(counts)
	current_count = 0
	for k in range(len(counts)):
		current_count += counts[k]
		if 1.0*current_count/total >= .5:
			return values[k]

def above(values,counts,threshold):
	total = np.sum(counts)
	current_count = 0
	for k in range(len(counts)):
		if values[k] > threshold:
			current_count += counts[k]
	return 1.0*current_count/total


mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='purplepants123',
    db='flight_performance')

c = mydb.cursor()

holidays = []

outfile = open('analysis_data/holiday_delays_mon_10.csv','w')

outfile.write('day_shift,time_bin,total_flights,avg_arr_delay,med_arr_delay,perc_above_0,perc_above_15,perc_above_30,perc_above_60\n')
f = open('analysis_data/holidays.csv','rU')
csv_data = csv.reader(f)
csv_data.next()
for row in csv_data:
	# if int(row[2]) > 2003 and row[3] == 'Thanksgiving Day':
	if int(row[2]) > 2003 and row[0] == 'Mon':
		holidays.append(row[5])

print holidays
print len(holidays)
start_time = time2.time()

# time_bin = time.strptime('00:00:00','%H:%M:%S')
time_bin = datetime.combine(date.today(), time(00,00))

for day_shift in range(-3,4):
	new_holidays = []
	for day in holidays:
		row_datetime = datetime.strptime(day,'%Y-%m-%d') + timedelta(days=day_shift)
		new_holidays.append(row_datetime.strftime('%Y-%m-%d'))
	for daytime in range(24):
		# print time_bin.strftime('%H:%M:%S')
		
		query_holidays = list(new_holidays)
		query_holidays.append(time_bin.strftime('%H:%M:%S'))
		query_holidays.append((time_bin + timedelta(minutes=59)).strftime('%H:%M:%S'))

		# print query_holidays

		format_strings = ','.join(['%s'] * len(holidays))
		c.execute("""SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE FL_DATE IN (%s) AND CRS_DEP_TIME >= %s AND CRS_DEP_TIME <= %s GROUP BY ARR_DELAY"""%(format_strings,'%s','%s'),tuple(query_holidays)) # 




		delay = []
		delay_count = []
		total_flights = 0

		for d in c.fetchall():
			total_flights += int(d[1])
			if d[0] == None:
				continue
			delay.append(d[0])
			delay_count.append(d[1])
			# print d[0],d[1]

		delay = np.array(delay,dtype=int)
		delay_count = np.array(delay_count,dtype=int)

		print day_shift,time_bin.strftime('%H:%M:%S'),total_flights,np.average(delay,weights=delay_count),median(delay,delay_count),\
			above(delay,delay_count,0),above(delay,delay_count,15),above(delay,delay_count,30),above(delay,delay_count,60)

		outfile.write('%i,%s,%i,%.4f,%i,%.4f,%.4f,%.4f,%.4f\n'%(day_shift,time_bin.strftime('%H:%M:%S'),total_flights,np.average(delay,weights=delay_count),median(delay,delay_count),\
			above(delay,delay_count,0),above(delay,delay_count,15),above(delay,delay_count,30),above(delay,delay_count,60)))

		time_bin = time_bin + timedelta(minutes=60)

print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		





