import requests
import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('UPSTOX_ACCESS_TOKEN')

url = 'https://api.upstox.com/v2/option/contract?instrument_key=NSE_INDEX%7CNifty%2050&expiry_date=2024-03-28'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}'
}

response = requests.get(url, headers=headers)
print(response.text)