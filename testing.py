import requests

url = "https://lat.motorsport.com/f1/results/2025/gp-de-espana-653362/?st=RACE"

response = requests.get(url)
print(response.text)