# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

from collections import OrderedDict

HTTP_CODES = {
    100: 'Continue',
    101: 'Switching Protocols',
    102: 'Processing',
    103: 'Early Hints',
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    203: 'Non-Authoritative Information',
    204: 'No Content',
    400: 'Bad Request',
    401: 'Unauthorized',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    422: 'Unprocessable Entity',
    429: 'Too Many Requests',
    500: 'Internal Server Error',
    503: 'Service Unavailable',
}

def success_response(data="", message="", code=200):
    return OrderedDict([
        ("status", "success"),
        ("code", code),
        ("detail", HTTP_CODES.get(code, "")),
        ("message", message),
        ("data", data)
    ]), code

def error_response(message="", code=400):
    return OrderedDict([
        ("status", "error"),
        ("code", code),
        ("detail", HTTP_CODES.get(code, "")),
        ("message", message),
        ("data", None)
    ]), code
