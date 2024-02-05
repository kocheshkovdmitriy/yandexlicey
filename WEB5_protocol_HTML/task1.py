import requests

ip_server = input().strip()
port = input().strip()
a = input().strip()
b = input().strip()

response = requests.get(
    url=f'{ip_server}:{port}',
    params={'a': a, 'b': b, 'format': 'json'}
).json()

print(*sorted(response['result']))
print(response['check'])