# coding:utf-8
"""
列表生成器
"""
def list_generator(raw_list, bulk_size):
    for i in range(0, len(raw_list), bulk_size):
        yield raw_list[i: i + bulk_size]

if __name__ == '__main__':
    test_list = [i for i in range(100)]
    bulk_size = 10

    for l in list_generator(test_list, bulk_size):
        print(len(l), l[0], l[-1])