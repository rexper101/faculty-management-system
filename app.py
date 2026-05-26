from flask import Flask
from extensions import db, login_manager
from config import Config
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'

    # ── User Loader ────────────────────────────────────────────────────
    @login_manager.user_loader
    def load_user(user_id):
        from models.models import AdminUser
        return AdminUser.query.get(int(user_id))

    # ── Blueprints ─────────────────────────────────────────────────────
    from routes.auth import auth_bp
    