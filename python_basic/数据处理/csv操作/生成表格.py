#coding:utf-8
import csv
csvfile = open('xxx.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow([u'col1', u'col2',u'col3',u'col4'])

res = []
for line in range(1,11):
    res.append(('line{}_value{}'.format(line, 1),
                'line{}_value{}'.format(line, 2),
                'line{}_value{}'.format(line, 3),
                'line{}_value{}'.format(line, 4),
                ))

writer.writerows(res)
csvfile.close()