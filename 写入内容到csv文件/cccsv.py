#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
csvfile = file('TmpUserList.csv', 'wb')
writer = csv.writer(csvfile)
# writer.writerow(['id', 'pwd', '有效期','分组','备注'])

# data = [
#   ('1', 'http://www.xiaoheiseo.com/', '小黑'),
#   ('2', 'http://www.baidu.com/', '百度'),
#   ('3', 'http://www.jd.com/', '京东')
# ]
data = []
for i in range(1000):
	data.append(('user'+str(i),'1','12h','tmp','Test'))
writer.writerows(data)
csvfile.close()