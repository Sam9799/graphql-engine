from flask import Flask
from flask import request, jsonify, abort

app = Flask(__name__)


def get_details_for_token(token):
    return {'X-Hasura-Role': 'user', 'X-Hasura-User-Id': '1'}


@app.route('/')
def hello():
    return 'webhook is running'


@app.route('/auth-webhook')
def auth_webhook():
    # get the auth token from Authorization header
    token = request.headers.get('Authorization')
    # similarly you can access all headers sent in the request. Hasura forwards
    # all request headers to the webhook

    # get the role and other variables for this token
    variables = get_details_for_token(token)

    return jsonify(variables) if variables is not None else abort(401)
