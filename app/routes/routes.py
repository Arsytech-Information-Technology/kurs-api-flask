# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

from flask import Blueprint
from app.controllers.kurs_controller import convert_currency
from app.controllers.welcome_controller import welcome

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return welcome()

v1_bp = Blueprint('v1', __name__, url_prefix='/v1')

@v1_bp.route('/kurs', methods=['POST'])
def handle_convert_currency():
    return convert_currency()
