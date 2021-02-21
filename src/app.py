from flask import Flask
import os

from create import create
from quote import quote
from status import status
from delete import delete
from update import update

app = Flask(__name__)

app.config['postmates_url'] = os.environ.get("POSTMATES_URL")
app.config['postmates_key'] = os.environ.get("POSTMATES_KEY")
app.config['postmates_base_path'] = os.environ.get("POSTMATES_BASE_PATH")
app.config['postmates_customer_id'] = os.environ.get("POSTMATES_CUSTOMER_ID")

app.register_blueprint(create)
app.register_blueprint(quote)
app.register_blueprint(delete)
app.register_blueprint(status)
app.register_blueprint(update)

@app.route('/healthz')
def healthz():
    if os.environ.get("ENVIRONMENT") == "development":
        env_dict = dict(os.environ)
        env_dict = {key:("REDACTED" if "KEY" in key else val) for key, val in env_dict.items()}
        return dict(env_dict)
    else:
        return "healthy"

if __name__ == '__main__':
   from waitress import serve
   serve(app, host='0.0.0.0', port=8080)
