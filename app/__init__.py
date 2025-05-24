# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

from flask import Flask
from .config import Config, CustomJSONProvider
from .routes.routes import main_bp, v1_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Override JSON provider
    app.json_provider_class = CustomJSONProvider
    app.json = app.json_provider_class(app)

    if not app.config.get("EXCHANGE_API_KEY"):
        raise RuntimeError("EXCHANGE_API_KEY is not set. Please check your .env file.")

    app.register_blueprint(main_bp)
    app.register_blueprint(v1_bp, url_prefix='/v1')

    return app
