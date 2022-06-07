from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        return {'query': json.loads(data)}
# 测试
URL = 'http://www.httpbin.org/get'
data = fetch_data(URL)
print(data)

print('ok')