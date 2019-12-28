# Import Dependencies
from flask import Flask
from waitress import serve

import uuid
import os
import re

# Intialize the flask app
app = Flask(__name__)

@app.after_request
def add_hostname_header(response):
        env_host = str(os.environ.get('HOSTNAME'))
        hostname = re.findall('[a-z]{3}-\d$', env_host)
        if hostname:
            response.headers["SP-LOCATION"] = hostname
        return response

@app.route('/')
def get_uuid():
    """ Function to respond to route
        Return UUID as a string response
    """
    return str(uuid.uuid4())

if __name__ == "__main__":
    serve(app, listen='*:8080')