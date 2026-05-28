from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models.models import LeaveRequest, Faculty
from app import db
from datetime import datetime

leaves_bp = Blueprint('leaves', __name__, url_prefix='/leaves')


def _parse_date(val):
    if not val:
        return None
    try:
        return datetime.strptime(val, '%Y-%m-%d').date()
    except ValueError:
        return None


@leaves_bp.route('/')
@login_required