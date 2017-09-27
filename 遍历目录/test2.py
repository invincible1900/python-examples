#coding=utf-8
#使用zipfile做目录压缩，解压缩功能
 
import os,os.path
import zipfile
import sys

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
           print f
        else:
            print 'not filepath!'
