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


mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='purplepants123',
    db='flight_performance')

c = mydb.cursor()

start_time = time.time()


plt.figure(1)

for k in range(1,2):
	print 'Analyzing month:',k
	c.execute("""SELECT ARR_DELAY,COUNT(ARR_DELAY) FROM flights WHERE YEAR = 1999 AND MONTH = %s \
		AND ARR_DELAY IS NOT NULL GROUP BY ARR_DELAY""",(k,)) # 

	delay = []
	delay_count = []

	for d in c.fetchall():
		delay.append(d[0])
		delay_count.append(d[1])
		# print d[0],d[1]

	delay = np.array(delay,dtype=int)
	delay_count = np.array(delay_count,dtype=int)
	# print delay
	# print delay_count
	print median(delay,delay_count)
	plt.subplot(2,2,k)
	plt.bar(delay,delay_count,width=.8)
	plt.xlim((-50,150))
	plt.title('Month %i'%(k))
	plt.annotate('Mean: %.2f'%np.average(delay,weights=delay_count),
		xy=(.8,.9),
		xycoords='axes fraction',
        horizontalalignment='left',
        verticalalignment='bottom',
        )


plt.show()
