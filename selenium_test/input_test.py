from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Ie()
file_path = 'file:///' + os.path.abspath('send_keys.html')

dr.get(file_path)

# copy content of A
dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'a'))
print '1'

dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'x'))
sleep(1)
# paste to B
dr.find_element_by_id('B').send_keys((Keys.CONTROL, 'v'))
sleep(1)
print '2'

# # send keys to A
dr.find_element_by_id('A').send_keys('watir', '-', 'webdriver', Keys.SPACE, 'is', Keys.SPACE, 'better')
sleep(2)
print '3'

dr.quit()