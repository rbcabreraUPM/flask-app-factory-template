from flask import Blueprint, render_template
from flask import current_app as app
from .models import Student
# Set up a Blueprint
student_bp = Blueprint('student_bp', __name__)


@student_bp.route('/')
def healthCheck():
    return 'Working mga sir!'