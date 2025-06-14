import os
import requests
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('UPSTOX_ACCESS_TOKEN')

url = 'https://api.upstox.com/v2/user/profile'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}
response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())