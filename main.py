import requests

cat_api = "https://catfact.ninja/fact"

request = requests.get(cat_api).json()
print(request)