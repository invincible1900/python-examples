#coding:utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

p = raw_input('Path: ')


# os.walk()返回的结果
print '*'*20 + 'os.walk()返回的结果'.decode('utf-8') + '*'*20
for r in os.walk(p):
	print r,type(r)
	for i in r:
		print i,type(i)
	print '-'*60
# 打印目录下所有文件名
print '*'*20 + '打印目录下所有文件名'.decode('utf-8') + '*'*20
for root,dirs,files in os.walk(p):
	for i in files:
		print i
	
# 打印目录下所有文件绝对路径名
print '*'*20 + '打印目录下所有文件绝对路径名'.decode('utf-8') + '*'*20
for root,dirs,files in os.walk(p):
	for i in files:
		print root + os.sep + i

# 打印所有子目录路径
print '*'*20 + '打印所有子目录路径'.decode('utf-8') + '*'*20
for root,dirs,files in os.walk(p):
	for i in dirs:
		print root + os.sep + i

# 打印目录结构
print '*'*20 + '打印目录结构'.decode('utf-8') + '*'*20
dirstruct = []
print os.walk(p),type(os.walk(p))
for root,dirs,files in os.walk(p):
	if root not in dirstruct:
		dirstruct.append(root)
		print root
	for i in dirs:
		if root + os.sep + i not in dirstruct:
			dirstruct.append(root + os.sep + i)
			print '\t'+root + os.sep + i
	for j in files:
		if root + os.sep + j not in dirstruct:
			dirstruct.append(root + os.sep + j)
			print '\t\t' + root + os.sep + j

anykey = raw_input('Press any key to exit...')