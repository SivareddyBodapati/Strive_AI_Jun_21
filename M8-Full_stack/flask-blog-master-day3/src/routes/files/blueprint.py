from flask import Blueprint,redirect,url_for,request,abort,send_from_directory
from src.constants import UPLOAD_FOLDER
import os

files_api_blueprint = Blueprint('files_api_blueprint', __name__)



@files_api_blueprint.route('/files', methods=['POST'])
def upload_file_route():
    return  redirect(url_for('home_blueprint.home_route'))



@files_api_blueprint.route('/files/<path:name>')
def serve_static_files(name):
    file_path = os.path.join(os.getcwd(),'src/static/uploads')
    return send_from_directory(file_path, name)
