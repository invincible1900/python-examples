from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

url = 'https://perbank.abchina.com/EbankSite/startup.do'
dr = webdriver.Ie()
dr.get(url)
# dr.find_element_by_id('username').send_keys((Keys.CONTROL, 'a'))
dr.find_element_by_id('username').send_keys('622220232545')

dr.find_element_by_id('powerpass_ieMsg').send_keys('622220232545')
dr.find_element_by_id('code').send_keys('2554')




sleep(10)

dr.quit()