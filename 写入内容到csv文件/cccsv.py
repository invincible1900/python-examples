#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
csvfile = file('TmpUserList.csv', 'wb')
writer = csv.writer(csvfile)

data = []
for i in range(1000):
	data.append(('user'+str(i),'1','12h','tmp','Test'))
writer.writerows(data)
csvfile.close()
