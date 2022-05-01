from pprint import pprint
from quart import Quart, jsonify, request
import secrets

app = Quart(__name__)


@app.route('/gentoken')
async def tokengen():
    token = secrets.token_urlsafe(30)
    print(token)
    return jsonify(invite=token)


app.run(port=5123, debug=True)