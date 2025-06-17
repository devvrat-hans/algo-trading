import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.getenv('UPSTOX_ACCESS_TOKEN')

url = "https://api-sandbox.upstox.com/v2/order/place"

payload = json.dumps({
  "quantity": 1,
  "product": "D",
  "validity": "DAY",
  "price": 0,
  "tag": "string",
  "instrument_token": "NSE_EQ|INE848E01016",
  "order_type": "MARKET",
  "transaction_type": "BUY",
  "disclosed_quantity": 0,
  "trigger_price": 0,
  "is_amo": False
})
headers = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)