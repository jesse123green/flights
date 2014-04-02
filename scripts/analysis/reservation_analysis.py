import MySQLdb
import sys,json
import time as time2
from datetime import datetime, timedelta, date, time
import numpy as np
import pylab as plt

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



# c.execute("""SELECT DEST, ORIGIN, AVG(CRS_ELAPSED_TIME) FROM FLIGHTS WHERE YEAR = 1988 AND ORIGIN IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','EWR','MCO','SLC','BOS','JFK','LGA','SEA','BWI') AND DEST IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','EWR','MCO','SLC','BOS','JFK','LGA','SEA','BWI') GROUP BY DEST,ORIGIN;""") # 

# reservations_old = {}

# for d in c.fetchall():
# 	reservations_old[d[0]+':'+d[1]] = float(d[2])

# json.dump(reservations_old,open('analysis_data/reservations_old.json','w'))

# c.execute("""SELECT DEST, ORIGIN, AVG(CRS_ELAPSED_TIME) FROM FLIGHTS WHERE YEAR = 2013 AND ORIGIN IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','EWR','MCO','SLC','BOS','JFK','LGA','SEA','BWI') AND DEST IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','EWR','MCO','SLC','BOS','JFK','LGA','SEA','BWI') GROUP BY DEST,ORIGIN;""") # 

# reservations_new = {}

# for d in c.fetchall():
# 	reservations_new[d[0]+':'+d[1]] = float(d[2])


# json.dump(reservations_new,open('analysis_data/reservations_new.json','w'))


reservations_old = json.load(open('analysis_data/reservations_old.json','r'))
reservations_new = json.load(open('analysis_data/reservations_new.json','r'))

differences = []

for key in reservations_new:
	if reservations_old.has_key(key):
		differences.append(reservations_new[key] - reservations_old[key])
		if (reservations_new[key] - reservations_old[key]) < 0:
			print key,reservations_new[key] - reservations_old[key]

print np.mean(differences)
plt.hist(differences,bins=50)
plt.grid()
plt.xlim((-40,40))
plt.show()



print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		



