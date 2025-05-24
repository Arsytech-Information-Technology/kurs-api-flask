# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

import requests
from flask import current_app

def get_exchange_rates(currency_from):
    api_key = current_app.config['EXCHANGE_API_KEY']
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency_from.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        return None
    return response.json()
