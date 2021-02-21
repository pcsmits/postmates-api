from flask import Blueprint, current_app

update = Blueprint('update', __name__)

@update.route('/update')
def update_main():
    return 'Updating delivery'
