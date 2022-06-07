import requests

r = requests.get('https://baidu.com/')
print(r.status_code)


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)