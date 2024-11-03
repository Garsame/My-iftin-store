from flask import Flask

app = Flask(__name__)

# Views import
from app.public import public_view
from app.User import user
from app import configuration
from app.Admin import admin


# Models import
from app.User import user_model