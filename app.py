from flask import Flask, request, jsonify
from models.user import User
app = Flask(__name__)

from routes.user_routes import user_bp
from routes.house_routes import house_bp
from routes.room_routes import room_bp
from routes.device_routes import device_bp

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(house_bp, url_prefix='/houses')
app.register_blueprint(room_bp, url_prefix='/rooms')
app.register_blueprint(device_bp, url_prefix='/devices')

if __name__ == '__main__':
    app.run(debug=True)