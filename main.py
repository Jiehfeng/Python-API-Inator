import os
from dotenv import load_dotenv
from app.server import server
from api.home import home_bp


# ENV File
load_dotenv('.env')


if __name__ == '__main__':
    server.register_blueprint(home_bp)
    
    server.run('localhost', port=8080, debug=True)

