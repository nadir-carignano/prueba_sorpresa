import os
from flask import (Flask,
                   render_template,
                   request,
                   jsonify)

from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from dotenv import load_dotenv
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import timedelta
from marshmallow import fields



db = SQLAlchemy(app)
migrate = Migrate(app , db )
jwt = JWTManager(app)
ma=Marshmallow(app)

class User(db.Model):
    __tablename__ ="user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False)

class Userbasicschema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    saludo_user = fields.Method("probando metodo")

    def probando_metodo(self,obj):
        return f"Hola {obj.username}"

class Usersadminschema(Userbasicschema):
    password = fields.String()
    

    
    

@app.route("/users")
def get_all_users():
    users = User.query.all()
    users_shema = Usersadminschema().dump(users, many=True)
    return jsonify(users_shema)



@app.route('/')
def hello():
	return "welcome to docker "

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/contacto")
def contacto():
	return render_template("contacto.html")

if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5005, debug = True)