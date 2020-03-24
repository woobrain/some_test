import requests
request_files = {'files': ('7.jpg', open('7.jpg', 'rb'), 'image/jepg')}
res = requests.post(url='http://47.102.252.183:51002/receipt_extraction/v1',files=request_files)
print(res.text)