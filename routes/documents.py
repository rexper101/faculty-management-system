import os
from flask import (Blueprint, render_template, redirect, url_for, request,
                   flash, current_app, send_from_directory, abort)
from flask_login import login_required
from werkzeug.utils import secure_filename
from models.models import Document, Faculty
from app import db

documents_bp = Blueprint('documents', __name__, url_prefix='/documents')

ALLOWED = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'txt'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED

