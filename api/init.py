from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.routes.auth import auth_bp
    from app.routes.properties import properties_bp
    from app.routes.reservations import reservations_bp
    from app.routes.reviews import reviews_bp

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(properties_bp, url_prefix='/api/v1/properties')
    app.register_blueprint(reservations_bp, url_prefix='/api/v1/reservations')
    app.register_blueprint(reviews_bp, url_prefix='/api/v1/reviews')

    return app
