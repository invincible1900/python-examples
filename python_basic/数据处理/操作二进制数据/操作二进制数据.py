# coding:utf-8
# python3
import struct

# 从文件获取一个bytes对象
with open('6g01', 'rb') as f:
    data = f.read()


def print_bytes(data):
    # 按字节打印bytes对象的每一个字节(16进制形式)
    for i in range(len(data)):
        print(i, data[i], bytes([data[i]]), hex(data[i]), type(hex(data[i])))


# 修改指定位置的字节数据
def change_byte(data, index, new_byte):
    """

    :param data: bytes
    :param index: int
    :param new_byte: unsigned int
    :return:
    """

    new_data = bytearray(data)

    new_data[index] = new_byte

    return new_data

def revers_bytes(b_data):
    """
    由于 ~ 操作符只能转换整型数据，不能对字节数据取反
    字节取反
    :param b_data: bytes 字节数据
    :return:
    """
    print(u'获得字节数据:', b_data)
    b2int = struct.unpack('B', b_data)[0]

    print(u'获得转换后的整型数据', b2int)

    re = ~b2int

    print(u'取反后的数据', re)

    if re < 0:
        int2b = struct.pack('i', re)
    else:
        int2b = struct.pack('I',re)
    print(u'转换成字节类型：', int2b)

    print(u'取反后的字节数据：', struct.pack('b', int2b[0]))
    return struct.pack('b', int2b[0])

def bytes_sum(a, b):
    """
    整型数据做加法运算
    :param a: int 0 ~ 255
    :param b: int 0 ~ 255
    :return: int 0 ~ 255
    """
    res = struct.pack('I', a + b)
    print('res', res[0])
    return res[0]


data = data[4:]
decode_data = bytearray(data)

for i in range(len(data)):
    # print(~(data[i] + 56))
    try:
        new_byte = revers_bytes(bytes_sum(data[i], 56))
    except:
        print(data[i] + 56)
        new_byte = b''

    decode_data = change_byte(decode_data, i, new_byte)
#
# for i in range(len(decode_data)):
#     print(decode_data[i])
#
# with open('6g01decode', 'wb') as f:
#     f.write(decode_data)

# new_byte = ord('g')
# print(change_byte(data, 0, new_byte))
# with open('gg01', 'wb') as f:
#     f.write(change_byte(data, 0, new_byte))

# print(138 & 0x000000ff)
# print(struct.pack('i', ~-138))
# data = data[4:]
# decode_data = bytearray(data)
# # print(type(data))
# # print(data[:4])
# # print(data[5])
# # # print(data[5])
# # x = 255
# # print(bytes([x]))
# #
# # print(hex(-1))

# print(struct.pack('i', ~-138))