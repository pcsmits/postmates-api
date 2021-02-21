from flask import Blueprint, current_app

import requests

create = Blueprint('create', __name__)

@create.route('/create')
def create_main():

    create_data = {
        'dropoff_address': '1900 W North Ave, Chicago, Il 60622',
        'pickup_address': '200 W Menomonee St, Chicago, Il 60614',
        'pickup_phone_number': '12625737234',
        'dropoff_phone_number': '12623094905',
        'manifest': 'small puzzle',
        'pickup_name': 'Parker Smits',
        'dropoff_name': 'Yuriy Onyskiv',
        'tip': '199',
    }

    header_data = {
        'Authorization': f'Basic {current_app.config["postmates_key"]}'
    }

    url = f'{current_app.config["postmates_url"]}\
{current_app.config["postmates_base_path"]}/\
{current_app.config["postmates_customer_id"]}/deliveries'

    resp = requests.post(url, data = create_data, headers = header_data)

    return f'{resp.text} ...{resp.status_code}'
