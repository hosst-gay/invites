from pprint import pprint
from quart import Quart, jsonify, request, render_template
import quart.flask_patch
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Quart(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/www/hosst/website/schema/invites.db'

class invites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invites = db.Column(db.String(100), nullable=False)


@app.route('/')
async def home():
    return await render_template("index.html")


@app.route('/gentoken')
async def tokengen():
    token = secrets.token_urlsafe(30)
    print(token)
    try:
        invite = invites(invites=token)
        
        db.session.add(invite)

        db.session.commit()
    except Exception as e:
        print(e)
    return jsonify(invite=token, status=200)


app.run(port=5123, debug=True)