# coding:utf-8
# 测试切换工作目录时候log文件的变化
import os
import loghandler

LOGGER = loghandler.setup_logging()
LOGGER.info('root path: ' + os.getcwd())

os.chdir('work_path1')
LOGGER = loghandler.setup_logging()
LOGGER.info('work_path1: ' + os.getcwd())

os.chdir('../work_path2')
LOGGER = loghandler.setup_logging()
LOGGER.info('work_path2: ' + os.getcwd())