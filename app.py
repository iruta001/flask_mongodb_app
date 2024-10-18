from flask import Flask
from flask_cors import CORS
from app.routes.user_routes import user_api
from app.config.config import config

def start_app():
    app = Flask(__name__)
    app.config.from_object(config) 
    CORS(app)
    app.register_blueprint(user_api, url_prefix = '/users')
    return app

if __name__ == '__main__':
    app = start_app()
    app.run(host = 'localhost', port = 8088, debug = True)