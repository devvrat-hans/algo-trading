import requests
import os
from dotenv import load_dotenv
load_dotenv()

UPSTOX_API_KEY = os.getenv('UPSTOX_API_KEY')
UPSTOX_API_SECRET = os.getenv('UPSTOX_API_SECRET')
UPSTOX_REDIRECT_URI = os.getenv('UPSTOX_REDIRECT_URI')

url = 'https://api.upstox.com/v3/login/auth/token/request/678d46e1-91ac-4b8d-925d-89c8e3015c2b'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = {
    'client_secret': f'{UPSTOX_API_SECRET}'
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())