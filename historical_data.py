import requests

url = "https://api.upstox.com/v2/historical-candle/:instrument_key/:interval/:to_date/:from_date"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)