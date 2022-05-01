from pprint import pprint
from quart import Quart, jsonify, request, render_template
import quart.flask_patch
import secrets

app = Quart(__name__)


@app.route('/')
async def home():
    return await render_template("index.html")


@app.route('/gentoken')
async def tokengen():
    token = secrets.token_urlsafe(30)
    print(token)
    return jsonify(invite=token, status=200)


app.run(port=5123, debug=True)