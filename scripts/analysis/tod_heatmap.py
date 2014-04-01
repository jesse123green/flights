import MySQLdb
import sys
import time as time2
from datetime import datetime, timedelta, date, time
import numpy as np

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

outfile = open('analysis_data/timeofday_2012.csv','w')

outfile.write('weekday,time_bin,total_flights,avg_arr_delay,med_arr_delay,perc_above_0,perc_above_15,perc_above_30,perc_above_60\n')


start_time = time2.time()

time_bin = datetime.combine(date.today(), time(00,00))

for weekday in range(0,7):
	for daytime in range(24):

		c.execute("""SELECT ARR_DELAY, COUNT(ARR_DELAY) FROM (SELECT ARR_DELAY,CRS_DEP_TIME FROM flights WHERE YEAR = 2012 AND WEEKDAY = %s) as YEARDAY WHERE CRS_DEP_TIME >= %s AND CRS_DEP_TIME <= %s GROUP BY ARR_DELAY""",(weekday,time_bin.strftime('%H:%M:%S'),(time_bin + timedelta(minutes=59)).strftime('%H:%M:%S'))) # 
		'''

		SELECT ARR_DELAY, COUNT(ARR_DELAY) FROM (SELECT ARR_DELAY,CRS_DEP_TIME FROM flights WHERE YEAR = 2013 AND WEEKDAY = 1) as YEARDAY WHERE CRS_DEP_TIME >= '00:00:00' AND CRS_DEP_TIME <= '00:30:00' GROUP BY ARR_DELAY



		'''

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

		print weekday,time_bin.strftime('%H:%M:%S'),total_flights,np.average(delay,weights=delay_count),median(delay,delay_count),\
			above(delay,delay_count,0),above(delay,delay_count,15),above(delay,delay_count,30),above(delay,delay_count,60)

		outfile.write('%i,%s,%i,%.4f,%i,%.4f,%.4f,%.4f,%.4f\n'%(weekday,time_bin.strftime('%H:%M:%S'),total_flights,np.average(delay,weights=delay_count),median(delay,delay_count),\
			above(delay,delay_count,0),above(delay,delay_count,15),above(delay,delay_count,30),above(delay,delay_count,60)))

		time_bin = time_bin + timedelta(minutes=60)


print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		



