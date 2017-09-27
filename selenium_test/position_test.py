#coding:utf-8
from selenium import webdriver

dr = webdriver.Ie()
# dr = webdriver.Firefox()



# dr.set_window_size(1000,200)
# dr.set_window_position(200,100)
dr.maximize_window()
dr.get('https://perbank.abchina.com/EbankSite/startup.do')
print dr.title
print dr.title == 'Internet Explorer 无法显示该网页'
print dr.title == u'Internet Explorer 无法显示该网页'
print dr.title == u'\u767e\u5ea6\u4e00\u4e0b\uff0c\u4f60\u5c31\u77e5\u9053'
# time.sleep(2)
# dr.get('https://mybank.icbc.com.cn/icbc/newperbank/perbank3/frame/frame_index.jsp')
# time.sleep(2)
# dr.get('https://ibsbjstar.ccb.com.cn/CCBIS/V6/common/login.jsp')

# dr.manage().window().setPosition(new Point(0,0));
# dr.manage().window().setSize(new Dimension(1024,768));
# 
import time
time.sleep(10)

dr.quit()