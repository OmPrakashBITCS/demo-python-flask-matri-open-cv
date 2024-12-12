from flask import Flask, Blueprint
from flask_restful import Api

from src.controllers.app_controller import AppController

app = Flask(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)

# Adding Resources
api.add_resource(AppController, '/app', '/app/<string:subpath>')

# Registering Blueprint
app.register_blueprint(api_bp)
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5006)
