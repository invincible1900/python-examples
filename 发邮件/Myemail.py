#coding:utf-8 
import smtplib;  
from email.mime.text import MIMEText  
  
def send_email(host,username,passwd,send_to,subject,content):  
    msg = MIMEText( content.encode('utf8'), _subtype = 'html', _charset = 'utf8')  
    msg['From'] = username  
    msg['Subject'] = u'%s' % subject  
    msg['To'] = ",".join(send_to)  
      
    try:  
        s = smtplib.SMTP_SSL(host,465)          
        s.login(username, passwd )  
        s.sendmail(username, send_to,msg.as_string())  
        print 'Send success...'
        s.close()  
    except Exception as e:  
        print 'Exception: send email failed', e  
  
if __name__ == '__main__':  
    host = 'smtp.sina.com.cn'  
    username = '395984722x@sina.com'  
    passwd = 'xxxxxx'  
    to_list = ['395984722x@sina.com','395984722@qq.com']  
    subject = "Test"  
    content = 'From python Test'  
    send_email(host,username,passwd,to_list,subject,content)  


# #coding:utf-8

# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# # 输入Email地址和口令:
# from_addr = raw_input('From: ')
# if not from_addr: from_addr = '395984722x@sina.com'
# password = raw_input('Password: ')
# if not password : password = 'xxxxxx'
# # 输入SMTP服务器地址:
# smtp_server = raw_input('SMTP server: ')
# if not smtp_server : smtp_server = 'smtp.sina.com.cn'
# # 输入收件人地址:
# to_addr = raw_input('To: ')
# if not to_addr: to_addr = '395984722x@sina.com'

# import smtplib
# server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()