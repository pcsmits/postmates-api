from flask import Blueprint, current_app, request

import requests

status = Blueprint('status', __name__)

@status.route('/status', methods=['GET', 'POST'])
def status_main():

    delivery_id = request.args.get('delivery_id', "No 'delivery_id' provided")

    header_data = {
        'Authorization': f'Basic {current_app.config["postmates_key"]}'
    }

    url = f'{current_app.config["postmates_url"]}\
{current_app.config["postmates_base_path"]}/\
{current_app.config["postmates_customer_id"]}/deliveries/\
{delivery_id}'

    resp = requests.get(url, headers = header_data)

    return f'{resp.text}'
