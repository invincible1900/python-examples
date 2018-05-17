import xmltodict

fp = u'解析xml/AndroidManifest.xml'
with open(fp, 'rb') as f:
    data = f.read()

ret = xmltodict.parse(data)
print(type(ret))

import json
print(json.dumps(ret, indent=2))

