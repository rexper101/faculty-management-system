import os
from datetime import timedelta

class Config:
    # ── Security ───────────────────────────────────────────────────────
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

    # ── Database ───────────────────────────────────────────────────────
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aniket%402004@localhost:3306/faculty_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
