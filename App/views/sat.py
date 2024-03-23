from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_user

sat = Blueprint('sat', __name__, template_folder='../templates')

@sat.route('/sat', methods=['GET'])
def index_page():
    return render_template('sat.html')
