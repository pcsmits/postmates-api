from flask import Blueprint, current_app

import requests

quote = Blueprint('quote', __name__)

@quote.route('/quote')
def quote_main():

    quote_data = {
        'dropoff_address': '10 W North Ave, Chicago, Il 60622',
        'pickup_address': '10 E Menomonee St, Chicago, Il 60614',
        'pickup_phone_number': '155551234',
        'dropoff_phone_number': '15559876',
    }

    header_data = {
        'Authorization': f'Basic {current_app.config["postmates_key"]}'
    }

    url = f'{current_app.config["postmates_url"]}\
{current_app.config["postmates_base_path"]}/\
{current_app.config["postmates_customer_id"]}/delivery_quotes'

    resp = requests.post(url, data = quote_data, headers = header_data)

    return f'{resp.text} ...{resp.status_code}'
