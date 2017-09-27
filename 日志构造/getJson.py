
l = """
MAC
IP
Auth_type
Auth_code
AUTH_TIME
"""
content = ''
l = l.split()
for item in l:
	# content = content +  "\""+item.upper()+"\"" + " : \"\",\n "
	content = content + ' '*5 + str(" \"%s\" : \"\",\n "%item.upper())

finalStr = """
head:
[
item:
{
""" + content[:-3]+content[-2:-1] + """
}
tail:
]
"""

print finalStr
# raw_input()

