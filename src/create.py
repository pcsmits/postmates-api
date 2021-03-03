from flask import Blueprint, current_app, request

import requests

create = Blueprint('create', __name__)

@create.route('/create', methods=['GET', 'POST'])
def create_main():

    dropoff_address = request.form.get('dropoff_address', "")
    pickup_address = request.form.get('pickup_address', "")
    dropoff_number = request.form.get('dropoff_number', "")
    pickup_number = request.form.get('pickup_number', "")
    dropoff_name = request.form.get('dropoff_name', "")
    pickup_name = request.form.get('pickup_name', "")
    manifest = request.form.get('manifest', "")
    tip = validate_tip(request.form.get('tip', 0))

    create_data = {
        'dropoff_address': '1900 W North Ave, Chicago, Il 60622',
        'pickup_address': '200 W Menomonee St, Chicago, Il 60614',
        'pickup_phone_number': f'{pickup_number}',
        'dropoff_phone_number': f'{dropoff_number}',
        'pickup_name': f'{pickup_name}',
        'dropoff_name': f'{dropoff_name}',
        'manifest': f'{manifest}',
        'tip': f'{tip}',
    }

    header_data = {
        'Authorization': f'Basic {current_app.config["postmates_key"]}'
    }

    url = f'{current_app.config["postmates_url"]}\
{current_app.config["postmates_base_path"]}/\
{current_app.config["postmates_customer_id"]}/deliveries'

    resp = requests.post(url, data = create_data, headers = header_data)

    return f'{resp.text} ...{resp.status_code}...{create_data}'


def validate_tip(tip):
    tip = str(tip).replace(".", "")
    tip = str(tip).replace("$", "")

    if int(tip) > 999:
        #Tip is too large
        tip = 199

    return tip
