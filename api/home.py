import os
from app.server import server
from flask import request, Blueprint


home_bp = Blueprint('home_bp', 'home_bp')


@home_bp.route('/', methods=['GET'])
def home():
    return f"<h1>LOAD ENV: {os.environ['MY-ENV']}</h1>"
