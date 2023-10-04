from flask import Blueprint

bp = Blueprint('core', __name__,
               template_folder='templates'
               ,static_folder='static'
               ,static_url_path='/core/static'
               )
@bp.route('/')
def index():
    return 'core index'