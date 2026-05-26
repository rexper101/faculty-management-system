from flask import (Blueprint, render_template, redirect, url_for, request,
                   flash, make_response)
from flask_login import login_required, current_user
from models.models import Salary, Faculty
from app import db
from datetime import date, datetime
from sqlalchemy import func

salary_bp = Blueprint('salary', __name__, url_prefix='/salary')
