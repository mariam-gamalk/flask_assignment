"""
Main Flask app entry point.
"""
from flask import Flask
from flask_cors import CORS
from models.product import db
from routers.category_router import category_bp
from routers.product_router import product_bp

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(category_bp)
app.register_blueprint(product_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)