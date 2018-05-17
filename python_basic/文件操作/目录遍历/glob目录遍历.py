# coding:utf-8
# 获得指定路径下符合条件的文件名列表
import glob

for file in glob.glob(r'../*.py'):
    print(file)