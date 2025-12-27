import requests

url = "http://localhost:3000"
params = {"a": 2, "b": 3}

r = requests.get(url, params=params)
print(r.text)
