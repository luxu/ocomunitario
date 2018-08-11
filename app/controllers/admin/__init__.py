from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin/page')

from . import views
