# coding:utf-8
# 类静态变量修改测试
# 注意包含 * 结果
class A:
    a = 123
    def changea(self, num):
        self.a = num


x = A()
y = A()
z = A()


print('+' * 50)
x.a = 234
print('x.a = 234')
print ('x.a: ', x.a)
print ('y.a: ', y.a)
print ('A().a: ', A().a)
print ('A.a: ', A.a)
print('+' * 50)
print()
print('+' * 50)
A().a = 456
print('A().a = 456')
print ('x.a: ', x.a, '*')
print ('y.a: ', y.a)
print ('A().a: ', A().a)
print ('A.a: ', A.a)
print('+' * 50)
print()
print('+' * 50)
A.a = 567
print('A.a = 567')
print ('x.a: ', x.a)
print ('y.a: ', y.a)
print ('A().a: ', A().a)
print ('A.a: ', A.a)
print('+' * 50)
print()
print('+' * 50)
z.changea(666)
print ('x.a: ', x.a)
print ('y.a: ', y.a)
print ('z.a: ', z.a, '*')
print ('A().a: ', A().a)
print ('A.a: ', A.a)
print('+' * 50)