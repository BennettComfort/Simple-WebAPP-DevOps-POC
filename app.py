# Import Dependencies
from flask import Flask
import uuid

# Intialize the flask app
app = Flask(__name__)

@APP.route('/')
def get_uuid():
    """ Function to respond to route
        Return UUID as a string response
    """
    return str(uuid.uuid4())

