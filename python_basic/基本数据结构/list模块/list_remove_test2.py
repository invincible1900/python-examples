# coding:utf-8
# 边循环边除列表中的元素

# 正确的方法：
a = [1,2,3,4,5,6,7,8]
for i in a:
    if i % 2 == 0:
        a.remove(i)
    print (a)

print(a)

print('*' * 100)

# 错误的方法：
# len(a)只会计算一次
# 不是所有元素都能遍历到
a = [1,2,3,4,4,5,6,7,8]
for i in range(len(a)):
    try:
        print('index:', i, 'value:', a[i], 'list:', a)
        if a[i] % 2 == 0:
            print(a[i], 'removed')
            a.remove(a[i])
    except Exception as e:
        print('index:', i, 'error:', e)

print(a)
