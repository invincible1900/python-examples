#coding:utf-8
#验证码识别
from PIL import Image
import pytesseract

vcode_path = ''
if not vcode_path:
	vcode_path = raw_input('Input vcode path:')


im = Image.open(vcode_path)

imgry = im.convert('L')
imgry.show()

threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()

print pytesseract.image_to_string(im)
print pytesseract.image_to_string(imgry)
print pytesseract.image_to_string(out)
im.close()
imgry.close()
out.close()