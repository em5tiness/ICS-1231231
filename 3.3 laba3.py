import requests 
url="https://google.com"
r=requests.get(url)
print(r.status_code)