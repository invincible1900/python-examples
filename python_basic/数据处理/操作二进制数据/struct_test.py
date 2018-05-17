import struct


"""
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

for i in range(256):
    print('='*100)

    print(i)

    byte_i = struct.pack('B', i)
    print(byte_i, type(byte_i))

    signed_i = struct.unpack('b', byte_i)
    print(signed_i, type(signed_i))

    unsigned_i = struct.unpack('B', byte_i)
    print(unsigned_i, type(unsigned_i))
    print('=' * 100)
    print('')

