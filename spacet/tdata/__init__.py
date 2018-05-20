from flask import Blueprint

bp = Blueprint('tdata', __name__, template_folder='templates',
               url_prefix='/tdata')

from spacet.tdata import remote, local
