import beeline

from beeline.middleware.flask import HoneyMiddleware
from flask import Flask

from local_secrets import honeycomb_api_key

beeline.init(
    writekey=honeycomb_api_key,
    dataset="taas",
    service_name="taas",
    debug=True,
)

app = Flask(__name__)
HoneyMiddleware(app, db_events=True)

@app.route("/hello")
def hello_world():
    return "Hello, World!"

