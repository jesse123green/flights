import MySQLdb
import sys, time
import pylab as plt
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

outfile = open('analysis_data/flight_history.csv','a')

# outfile.write('year,month,total_flights,avg_arr_delay,med_arr_delay,perc_above_0,perc_above_15,perc_above_30,perc_above_60\n')
start_time = time.time()

for year in range(1995,2015):
	for month in range(1,13):
		print 'Analyzing %i-%i'%(year,month)
		c.execute("""SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE YEAR = %s AND MONTH = %s \
			GROUP BY ARR_DELAY""",(year,month)) # 

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
		if len(delay) == 0:
			continue
		delay = np.array(delay,dtype=int)
		delay_count = np.array(delay_count,dtype=int)

		# print median(delay,delay_count)
		# print above(delay,delay_count,0)
		# print above(delay,delay_count,15)
		# print above(delay,delay_count,30)
		outfile.write('%i,%i,%i,%.4f,%i,%.4f,%.4f,%.4f,%.4f\n'%(year,month,total_flights,np.average(delay,weights=delay_count),median(delay,delay_count),\
			above(delay,delay_count,0),above(delay,delay_count,15),above(delay,delay_count,30),above(delay,delay_count,60)))
		





