import os
import requests
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('UPSTOX_ACCESS_TOKEN')

url = 'https://api.upstox.com/v2/charges/brokerage'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

params = {
    'instrument_token': 'NSE_FO|35271',
    'quantity': '10',
    'product': 'I',
    'transaction_type': 'BUY',
    'price': '1400'
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.json())