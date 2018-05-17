def yield_test():
    print('step 1.......')
    res = yield 10
    print('step 2.......', res)


gen = yield_test()
data = gen.send(None) #next(gen)  (1)
print('yield out .....', data)
gen.send(20)
# print ('yield out .....', data)