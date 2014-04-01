import csv
import MySQLdb
import glob, sys, time
from datetime import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='purplepants123',
    db='flight_performance')

cursor = mydb.cursor()


start_time = time.time()
x = 0
for folder in glob.glob("../data/*"):
	for f in glob.glob(folder + '/*.csv'):

		csv_data = csv.reader(file(f))
		csv_data.next()
		for row in csv_data:
			x += 1
			row = row[:-1]
			row_datetime = datetime.strptime(row[0],'%Y-%m-%d')
			year = row[0][:4]
			month = row[0][5:7]
			row.append(year)
			row.append(month)
			row.append(str(row_datetime.weekday()))
			for k in range(len(row)):
				if row[k] == '':
					row[k] = None
			for k in [5,6,9,10,12,13,27]:
				if row[k] != None:
					row[k] = row[k][:2] + ':' + row[k][2:]

			# # temp = ["FL_DATE","UNIQUE_CARRIER","CARRIER","ORIGIN","DEST","CRS_DEP_TIME","DEP_TIME","DEP_DELAY","TAXI_OUT","WHEELS_OFF","WHEELS_ON","TAXI_IN","CRS_ARR_TIME","ARR_TIME","ARR_DELAY","CANCELLED","CANCELLATION_CODE","DIVERTED","CRS_ELAPSED_TIME","ACTUAL_ELAPSED_TIME","AIR_TIME","DISTANCE","CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY","SECURITY_DELAY","LATE_AIRCRAFT_DELAY","FIRST_DEP_TIME","TOTAL_ADD_GTIME","LONGEST_ADD_GTIME","YEAR","MONTH","WEEKDAY"]
			# for r in range(len(temp)):
			# 	print temp[r],row[r]
			# print row
			# print len(row)
			cursor.execute("""INSERT IGNORE INTO flights(FL_DATE,UNIQUE_CARRIER,CARRIER,ORIGIN,DEST,CRS_DEP_TIME,DEP_TIME,DEP_DELAY,TAXI_OUT,WHEELS_OFF,WHEELS_ON,TAXI_IN,CRS_ARR_TIME,ARR_TIME,ARR_DELAY,CANCELLED,CANCELLATION_CODE,DIVERTED,CRS_ELAPSED_TIME,ACTUAL_ELAPSED_TIME,AIR_TIME,DISTANCE,CARRIER_DELAY,WEATHER_DELAY,NAS_DELAY,SECURITY_DELAY,LATE_AIRCRAFT_DELAY,FIRST_DEP_TIME,TOTAL_ADD_GTIME,LONGEST_ADD_GTIME,YEAR,MONTH,WEEKDAY)\
				VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
				row)
		mydb.commit()
		print 'Completed file %s after %.2f minutes'%(f,(time.time() - start_time)/60.)


#close the connection to the database.
cursor.close()
print "Done"