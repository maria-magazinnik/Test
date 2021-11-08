import requests

print(requests.post('http://127.0.0.1:9500', data='Post').content)
print(requests.get('http://127.0.0.1:9500', data='Get').content)
print(requests.put('http://127.0.0.1:9500', data='Put').content)
print(requests.delete('http://127.0.0.1:9500', data='Delete').content)
