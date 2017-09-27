import zipfile
import os
startdir = raw_input('Dirpath: ')
dirfather,dirname = os.path.split(startdir)
os.chdir(dirfather)
print os.getcwd()	
print dirname
if not os.path.isdir(startdir):
	tgt = startdir.split('.')[0] +'.zip'
	f = zipfile.ZipFile(tgt,'w',zipfile.ZIP_DEFLATED)
	f.write(dirname)
else:
	tgt = dirname +'.zip'
	print tgt
	f = zipfile.ZipFile(tgt,'w',zipfile.ZIP_DEFLATED)
	for dirpath, dirnames, filenames in os.walk(startdir):
	    for filename in filenames:
	        f.write(os.path.join(dirpath,filename))
	        # f.write(os.path.join(dirname,filename))
f.close()