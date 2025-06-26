import requests
import os
from dotenv import load_dotenv
load_dotenv()

UPSTOX_API_KEY = os.getenv('UPSTOX_API_KEY')
UPSTOX_API_SECRET = os.getenv('UPSTOX_API_SECRET')
UPSTOX_REDIRECT_URI = os.getenv('UPSTOX_REDIRECT_URI')

url = 'https://api.upstox.com/v2/login/authorization/token'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'code': 'ababababaaa',
    'client_id': f'{UPSTOX_API_KEY}',
    'client_secret': f'{UPSTOX_API_SECRET}',
    'redirect_uri': f'{UPSTOX_REDIRECT_URI}',
    'grant_type': 'authorization_code',
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())