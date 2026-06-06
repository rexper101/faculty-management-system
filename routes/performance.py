from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required
from models.models import PerformanceReview, Faculty
from app import db
from sqlalchemy import func

performance_bp = Blueprint('performance', __name__, url_prefix='/performance')


@performance_bp.route('/')
@login_required
def index():
    faculty_list = Faculty.query.filter_by(status='Active').order_by(Faculty.first_name).all()
    reviews = (PerformanceReview.query
               .join(Faculty)
               .order_by(PerformanceReview.review_year.desc())
               .all())
    # Average per faculty for summary
    avg_data = (db.session.query(Faculty.first_name, Faculty.last_name,
                                  func.avg(PerformanceReview.rating))
                .join(PerformanceReview, PerformanceReview.faculty_id == Faculty.faculty_id)
                .group_by(Faculty.faculty_id)
                .all())
    return render_template('performance/index.html',
                           reviews=reviews, faculty_list=faculty_list,
                           avg_data=avg_data)


@performance_bp.route('/add', methods=['POST'])
@login_required
def add():
    rev = PerformanceReview(
        faculty_id  = request.form.get('faculty_id'),
        review_year = request.form.get('review_year'),
        rating      = request.form.get('rating'),
        remarks     = request.form.get('remarks', '').strip() or None,
    )
    db.session.add(rev)
    db.session.commit()
    flash('Performance review added.', 'success')
    return redirect(url_for('performance.index'))

