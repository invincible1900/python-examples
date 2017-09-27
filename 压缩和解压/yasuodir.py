import zipfile
import os
startdir = raw_input('Dirpath: ')
dirfather,dirname = os.path.split(startdir)
os.chdir(dirfather)
tgt = dirname +'.zip'
print tgt
f = zipfile.ZipFile(tgt,'w',zipfile.ZIP_DEFLATED)
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        f.write(os.path.join(dirpath,filename))
f.close()