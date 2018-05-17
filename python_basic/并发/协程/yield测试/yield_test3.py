# # def g(x):
# #     yield from range(x, 0, -1)
# #     yield from range(x)
#
# def f(x):
#     for i in range(x,0,-1):
#         yield i
#         print('y1')
#
#     for j in range(x):
#         yield j
#         print('y2')
#
#
# # print (list(g(6)))
# # l = list(f(6))
# # print l
#
# # print (list(f(6)))
#
#
# l = f(6)
# print l.next()
# print l.next()
# print l.next()
#
#
# # for i in f(6):
# #     print (i)