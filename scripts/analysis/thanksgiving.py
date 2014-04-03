import MySQLdb
import sys, csv, json
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

outfile = {}
holidays = []

f = open('analysis_data/holidays.csv','rU')
csv_data = csv.reader(f)
csv_data.next()
for row in csv_data:
	if int(row[2]) > 2003 and row[3] == 'Thanksgiving Day':
		holidays.append(row[5])


weekdaynames = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

for day_shift in range(-2,1):
	new_holidays = []
	for day in holidays:
		row_datetime = datetime.strptime(day,'%Y-%m-%d') + timedelta(days=day_shift)
		new_holidays.append(row_datetime.strftime('%Y-%m-%d'))
	print tuple(new_holidays)
	format_strings = ','.join(['%s'] * len(new_holidays))
	c.execute("""SELECT DEST, ORIGIN, COUNT(ARR_DELAY), AVG(ARR_DELAY), AVG(AIR_TIME) FROM FLIGHTS WHERE FL_DATE IN (%s) AND ORIGIN IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','MCO','SLC','BOS','JFK','SEA','BWI') AND DEST IN ('ATL','ORD','DFW','DEN','LAX','IAH','PHX','SFO','DTW','CLT','MSP','LAS','MCO','SLC','BOS','JFK','SEA','BWI') GROUP BY DEST,ORIGIN;"""%(format_strings),tuple(new_holidays)) # 
	'''



	'''
	current_day = row_datetime.weekday()

	for d in c.fetchall():
		print current_day,d[0],d[1],d[2]
		if int(d[2]) == 0:
			continue
		if not(outfile.has_key(d[0])):
			outfile[d[0]] = {}
		if not(outfile[d[0]].has_key(d[1])):
			outfile[d[0]][d[1]] = {}
		outfile[d[0]][d[1]][weekdaynames[current_day]] = {}
		outfile[d[0]][d[1]][weekdaynames[current_day]]['ratio'] = (float(d[3]) + float(d[4]))/float(d[4])
		outfile[d[0]][d[1]][weekdaynames[current_day]]['numFlights'] = int(d[2])
	# print outfile
print outfile['DEN']['LAX']
counts = []

for key in outfile:
	# print key
	for key2 in outfile[key]:
		ratios = []
		for key3 in ['Tue','Wed','Thu']:
			if outfile[key][key2].has_key(key3):
				ratios.append(outfile[key][key2][key3]['ratio'])
				counts.append(outfile[key][key2][key3]['numFlights'])
		# print key,key2,outfile[key][key2]
		outfile[key][key2]['rmax'] = np.max(ratios)
		outfile[key][key2]['rmin'] = np.min(ratios)

print 'Max number of flights:',np.max(counts)
print 'Min number of flights:',np.min(counts)

# sys.exit()

json.dump(outfile,open('analysis_data/thanksgiving/thanksgiving_flights.json','w'))


print 'Run Time: %.2f mins'%((time2.time() - start_time)/60.)		



