from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

sat_views = Blueprint('sat_views', __name__, template_folder='../templates')

@sat_views.route('/sat', methods=['GET'])
def index_page():
    return render_template('sat.html')
