#coding=utf-8
#使用zipfile做目录压缩，解压缩功能
 
import os,os.path
import zipfile
import sys 


def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()
 
 
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:            
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
 
#一个目录下所有非目录文件的文件名列表，或某个绝对路径的文件的文件名
def get_files(ps_path):
    files = []
    if os.path.isfile(ps_path):
        pa_path=os.path.split(ps_path)
        print ' '*32,pa_path[0]
        print pa_path[1]
        files.append(ps_path);
    else:
        if os.path.isdir(ps_path):
            for ps_one in os.walk(ps_path):
                print ' '*32,ps_one[0]
                files.append(ps_one[0])
                for ps_file in ps_one[2]:
                    files.append(ps_path+os.sep+ ps_file)
                    print ps_file
    print files
    return files


if __name__ == '__main__':
    while(1):
        f = []
        ls_file=''
        if len(sys.argv)>1:
            ls_file=sys.argv[1]

        if ''==ls_file:
            ls_file=raw_input('filepath:')

        if os.path.exists(ls_file):
            f = get_files(ls_file)
            for filename in f[1:]:
                print f[0],filename
                unzip_file(filename,f[0]);
        else:
            print 'not filepath!'
   
   
    # unzip_file(r'E:/Users/xxx.zip',r'E:/Users')