from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from app import app


def error_response(status_code, message):
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "unknown error")}
    if message:
        payload["message"] = message
    return payload, status_code

def bad_request():
    return error_response(400, message)

@app.errorhandler(HTTPException)
def handle_exception(e):
    return error_response(e.code)