import MySQLdb
import sys,csv
import time as time2
from datetime import datetime, timedelta, date, time
import numpy as np

# def median(values,counts):
# 	total = np.sum(counts)
# 	current_count = 0
# 	for k in range(len(counts)):
# 		current_count += counts[k]
# 		if 1.0*current_count/total >= .5:
# 			return values[k]

# def above(values,counts,threshold):
# 	total = np.sum(counts)
# 	current_count = 0
# 	for k in range(len(counts)):
# 		if values[k] > threshold:
# 			current_count += counts[k]
# 	return 1.0*current_count/total


# mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='purplepants123',
#     db='flight_performance')

# c = mydb.cursor()

start_time = time2.time()

outfile = open('analysis_data/tod/timeofday_all.csv','w')
outfile.write('weekday,time_bin,total_flights,avg_arr_delay,med_arr_delay,perc_above_0,perc_above_15,perc_above_30,perc_above_60\n')
d = []
daytime = []

for ayear in range(2004,2014):
	print ayear
	datafile = open('analysis_data/tod/timeofday_' + str(ayear) + '.csv','r')
	csv_data = csv.reader(datafile)
	csv_data.next()
	for row in csv_data:
		d.append(row[2:])
		daytime.append(row[0] + row[1])
d = np.array(d,dtype=float)
daytime = np.array(daytime,dtype=str)

unique_daytime = np.unique(daytime)



for a_daytime in unique_daytime:
	dtI = (daytime == a_daytime)
	outfile.write('%s,%s,%i,%.4f,0,%.4f,%.4f,%.4f,%.4f\n'%(a_daytime[0],a_daytime[1:],np.sum(d[dtI,0]),np.average(d[dtI,1],weights=d[dtI,0])\
		,np.average(d[dtI,3],weights=d[dtI,0]),np.average(d[dtI,4],weights=d[dtI,0]),np.average(d[dtI,5],weights=d[dtI,0]),np.average(d[dtI,6],weights=d[dtI,0])))


outfile.close()

print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		



