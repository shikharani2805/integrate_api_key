import requests

# res = requests.get('https://ipinfo.io/')

# API Access Key of ipstack

res = requests.get('http://api.ipstack.com/103.103.161.21?access_key=8d1b292fc2de76b0666a4a821422a0b0')

data = res.json()
print(data)


