# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

from app.utils.response import success_response

def welcome():
    return success_response(message="Welcome to Arsytech Kurs API version 1 - Flask")
