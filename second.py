from flask import Blueprint

second_app = Blueprint('second_app', __name__)

@second_app.route('/second')
def second():
    return 'Hello from second!'
