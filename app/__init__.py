from flask import Flask, render_template
from flask_cors import CORS
from app.services.llm_service import LLMService
import logging
import sys


def create_app():
    app = Flask(__name__)

    # initialize CORS
    CORS(app)

    # set up logging
    app.logger.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.propagate = False

    app.logger.info("The app is starting...")

    # initialize llm service
    with app.app_context():
        llm_service = LLMService()
        app.llm_service = llm_service

    # register blueprints
    from app.api import chat_bp, analysis_bp
    app.register_blueprint(chat_bp)
    app.register_blueprint(analysis_bp)

    app.logger.info("The app is initialized...")

    # the main page
    @app.route('/')
    def index():
        app.logger.info("Rendering index page")
        return render_template('index.html')

    return app
