import MySQLdb
import sys, time
# import pylab as plt
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

# outfile = open('analysis_data/flight_history.csv','a')

# outfile.write('year,month,total_flights,avg_arr_delay,med_arr_delay,perc_above_0,perc_above_15,perc_above_30,perc_above_60\n')


start_time = time.time()

# SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE YEAR = 2013 AND WEEKDAY = 1 AND CRS_DEP_TIME < '10:05:00' AND CRS_DEP_TIME >= '10:00:00' GROUP BY ARR_DELAY;

c.execute("""SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE YEAR = 2013 AND WEEKDAY = %s AND CRS_DEP_TIME < '10:30:00' AND CRS_DEP_TIME >= '10:00:00' GROUP BY ARR_DELAY""",(1,)) # 




delay = []
delay_count = []
total_flights = 0
for d in c.fetchall():
	print d


print 'Run Time: %.2f mins'%((time.time() - start_time)/60.)		





