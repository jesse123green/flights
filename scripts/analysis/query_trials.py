import csv
import MySQLdb
import glob, sys, time
from datetime import datetime

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='purplepants123',
    db='flight_performance')

c = mydb.cursor()


start_time = time.time()



# c.execute("""SELECT COUNT(*) FROM flights GROUP BY YEAR""") #
# c.execute("""SELECT MONTH,YEAR,COUNT(*) FROM flights GROUP BY MONTH,YEAR""") #
# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM flights WHERE YEAR = 1988 GROUP BY MONTH,YEAR""") # 1.24
# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM flights WHERE YEAR = 1988 OR YEAR = 1989 GROUP BY MONTH,YEAR LIMIT 100""") # 1.89



# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM flights WHERE YEAR = 1988 OR YEAR = 1989 OR YEAR = 1990 GROUP BY MONTH,YEAR""") # 1.89
# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM flights WHERE YEAR < 1995 GROUP BY MONTH,YEAR""") # 20+
# c.execute("""SELECT MONTH,AVG(ARR_DELAY) FROM flights WHERE YEAR = 1988 OR YEAR = 1989 GROUP BY MONTH""") # 



# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM (SELECT MONTH,YEAR,ARR_DELAY FROM flights WHERE YEAR = 1988 LIMIT 100000) AS flight_sub GROUP BY MONTH, YEAR""") #
# c.execute("""SELECT MONTH,YEAR,COUNT(*),AVG(ARR_DELAY) FROM flights WHERE YEAR = 1999 GROUP BY MONTH,YEAR""") # 5 min

## Histogram for a month of airline delays

# c.execute("""SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE YEAR = 1999 AND MONTH = 1 GROUP BY ARR_DELAY""") # 

# c.execute("""SELECT MONTH,YEAR,AVG(ARR_DELAY) FROM flights WHERE YEAR = 1999 GROUP BY MONTH,YEAR""") # 
c.execute("""SELECT MONTH,YEAR,MEDIAN(ARR_DELAY) FROM flights WHERE YEAR = 1999 GROUP BY MONTH,YEAR""") # 1.24

for d in c.fetchall():
	print d[0],d[1],d[2]

# for d in c.fetchall():
# 	print d[0],d[1],d[2],d[3]


print 'Run Time: %.2f mins'%((time.time() - start_time)/60.)
#close the connection to the database.
c.close()
print "Done"