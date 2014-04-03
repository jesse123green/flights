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

start_time = time2.time()

outfile = open('analysis_data/thanksgiving/thanksgiving_all.csv','w')

d = []
paths = []

for ayear in range(2004,2014):
	print ayear
	datafile = open('analysis_data/thanksgiving_' + str(ayear) + '.csv','r')
	datafile.next()
	for row in datafile:
		d.append(row[3:])
		paths.append(row[1] + row[2])

d = np.array(d,dtype=float)
paths = np.array(paths,dtype=str)

unique_paths = np.unique(paths)

for a_path in unique_paths:




print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		



