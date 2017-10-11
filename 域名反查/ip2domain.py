import requests

ip = ''
while not ip:
	ip = raw_input('Input ip: ')

url = "https://domains.yougetsignal.com/domains.php"
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"remoteAddress\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"%ip
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
res = eval(response.text)

def get_item(one_list):
	for i in one_list:
		if isinstance(i,list):
			get_item(i)
		elif i:
			print i


if 'domainArray' in res.keys():
	get_item(res['domainArray'])