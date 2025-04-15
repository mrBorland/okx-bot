
import requests
import time
import hmac
import hashlib

API_KEY = '8ce4bd62-9328-495e-9556-2bf1107b3ac2'
API_SECRET = 'AB2C36344430A6080F3C5645155074B3'
PASSPHRASE = 'Slipknot221989@'

def generate_signature(timestamp, method, request_path, body=''):
    message = f'{timestamp}{method}{request_path}{body}'
    return hmac.new(API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()

def auto_withdraw():
    url = "https://www.okx.com/api/v5/asset/withdrawal"
    amount = "2.00"
    timestamp = str(time.time())

    body = {
        "ccy": "USDT",
        "amt": amount,
        "dest": "4",
        "toAddr": "TTb8QfyLAsXtTyZZ1SZiCUZt6H6PfJb3Wo",
        "chain": "USDT-TRC20"
    }

    headers = {
        "OK-ACCESS-KEY": API_KEY,
        "OK-ACCESS-SIGN": generate_signature(timestamp, "POST", "/api/v5/asset/withdrawal", str(body).replace("'", '"')),
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": PASSPHRASE,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=body, headers=headers)
    print("Результат виводу:", response.status_code, response.text)
