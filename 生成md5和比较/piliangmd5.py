#coding:utf-8

#md5check.py
#读文件,转成md5码
#如没有文件路径，则询问
#是文件，返回md5码
#是路径把其下所有文件返回md5码
#参考：http://www.joelverhagen.com/blog/2011/02/md5-hash-of-file-in-Python/


import hashlib
import sys
import os

def md5Checksum(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    fh.close()
    return m.hexdigest()


def pathispath(ps_path):
    if os.path.isfile(ps_path):
        pa_path=os.path.split(ps_path)
        print ' '*32,pa_path[0]
        print md5Checksum(ps_path),
        print pa_path[1]
    else:
        if os.path.isdir(ps_path):
            for ps_one in os.walk(ps_path):
                print ' '*32,ps_one[0]
                for ps_file in ps_one[2]:
                    print md5Checksum(os.path.join(ps_one[0],ps_file)),
                    print ps_file


if __name__ == '__main__':
	while(1):
		ls_file=''
		if len(sys.argv)>1:
			ls_file=sys.argv[1]

		if ''==ls_file:
			ls_file=raw_input('filepath:')

		if os.path.exists(ls_file):
			#if os.path.isfile(ls_file):
			#    print md5Checksum(ls_file)
			#else:
			#    if os.path.isdir(ls_file):
			#        pathispath(ls_file)
			pathispath(ls_file)
		else:
			print 'not filepath!'