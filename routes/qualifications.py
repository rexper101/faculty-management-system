from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from models.models import Qualification, Faculty
from app import db
from datetime import datetime

qualifications_bp = Blueprint('qualifications', __name__, url_prefix='/qualifications')


@qualifications_bp.route('/<int:faculty_id>')
@login_required
def index(faculty_id):
    fac  = Faculty.query.get_or_404(faculty_id)
    quals = Qualification.query.filter_by(faculty_id=faculty_id).order_by(
        Qualification.passing_year.desc()).all()
    return render_template('qualifications/index.html', faculty=fac, quals=quals)


@qualifications_bp.route('/<int:faculty_id>/add', methods=['POST'])
@login_required