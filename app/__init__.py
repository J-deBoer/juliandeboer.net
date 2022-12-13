from flask import Flask
from flask_bootstrap import Bootstrap
import os


project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
bootstrap = Bootstrap(app)

from app import routes, errors