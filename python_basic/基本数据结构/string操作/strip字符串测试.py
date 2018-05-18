# coding:utf-8
"""
测试字符串的strip()函数
当参数是字符串的时候会出现神奇的结果
"""
print('*' * 100)
a = '61.15.0.0/16'
print("print('61.15.0.0/16'.strip('/16')):", a.strip('/16'), '!!!!!')
print("print('61.15.0.0/16'.strip('16')):", a.strip('16'), '!!!!!')
print("print('61.15.0.0/16'.strip('61')):", a.strip('61'), '!!!!!')

print('*' * 100)
a = '61.15.0.0/61'
print("print('61.15.0.0/61'.rstrip('/16')):", a.rstrip('/16'), '!!!!!')
print('*' * 100)


a = a.strip('6')
print("print('61.15.0.0/16'.strip('6')):", a)

a = a.strip('1')
print("print('1.15.0.0/1'.strip('1')):", a)

a = a.strip('/')
print("print('.15.0.0/'.strip('/')):", a)
print('*' * 100)

a = '61.15.0.0/16'
print("print('61.15.0.0/16'.rstrip('/16')):", a.rstrip('/16'))

print('*' * 100)


a = '12345654321'
print("print('12345654321'.strip('12')):", a.strip('12'), '!!!!!')
print("print('12345654321'.rstrip('12')):", a.rstrip('12'), '!!!!!')
print("print('12345654321'.rstrip('21')):", a.rstrip('21'))
print('*' * 100)
