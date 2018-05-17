import struct
struct_map = """
struct中支持的格式如下表：

Format	C Type	Python	字节数
    x 	pad byte 	no value 	1
    c 	char 	string of length 1 	1           
    b 	signed char 	integer 	1           -128 ~ 127    
    B 	unsigned char 	integer 	1           0 ~ 255
    ? 	_Bool 	bool 	1
    h 	short 	integer 	2
    H 	unsigned short 	integer 	2
    i 	int 	integer 	4
    I 	unsigned int 	integer or lon 	4
    l 	long 	integer 	4
    L 	unsigned long 	long 	4
    q 	long long 	long 	8
    Q 	unsigned long long 	long 	8
    f 	float 	float 	4
    d 	double 	float 	8
    s 	char[] 	string 	1
    p 	char[] 	string 	1
    P 	void * 	long 	　"""

# print(u'\n说明：\n\tpack方法把指定类型数据转换成bytes类型, \n\tunpack方法把bytes类型转换成指定类型')
# print(struct_map)
#
#
# byte_a = b'\xf0'
#
# print(u'\n原始字节对象:\n', byte_a, type(byte_a))
# print('')
#
#
# # 转无符号整数(0~255 int)类型
# char_a = struct.unpack('B', byte_a)
# print(u'转无符号整数(0~255 int)类型:\n', char_a[0], type(char_a[0]), struct.pack('I',char_a[0]))
# print('')
#
# # 转有符号整数(-128~127)类型
# signed_char_a = struct.unpack('b', byte_a)
# print(u'转有符号整数(-128~127)类型:\n', signed_char_a[0], type(signed_char_a[0]), struct.pack('i',signed_char_a[0]))
# print('')
#
# print("说明:\n\t负数在计算机中由正数按位取反加一表示，例如 1('\\x01\\x00\\x00\\x00') 按位取反加一得到 -1('\\xff\\xff\\xff\\xff')\n")
#
# # 无符号整数取反得到有符号整数
# r_int_a = ~char_a[0]
# print(u'无符号整数取反得到有符号整数:\n', r_int_a, type(r_int_a), struct.pack('i', r_int_a))
# print('')
#
# # 有符号整数转无符号整数
# unsigned_r_int_a = struct.unpack('I', struct.pack('i', r_int_a))[0]
# print(u'有符号整数转无符号整数:\n', unsigned_r_int_a, type(unsigned_r_int_a), struct.pack('I', unsigned_r_int_a))
# print('')
#
# # 取整数的最低位
# print(u'取整数的最低位:')
# print('整数:',unsigned_r_int_a, struct.pack('I', unsigned_r_int_a))
# print('最低位:', struct.pack('I', unsigned_r_int_a)[0], struct.pack('b', struct.pack('I', unsigned_r_int_a)[0]))

def revers_bytes(b_data):
    """
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

print(revers_bytes(b'\xf0'))