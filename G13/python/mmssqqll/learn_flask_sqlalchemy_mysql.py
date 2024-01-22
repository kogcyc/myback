from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kogswell:p2p2p2p2@kogswell.mysql.pythonanywhere-services.com/kogswell$matt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://matt:kikikiki@raspberrypi.local/matt'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Create tables
#with app.app_context():
    #db.create_all()

# Perform database operations
#user = User(username='example_user')
#db.session.add(user)
#db.session.commit()

# Query the database
all_users = User.query.all()
for user in all_users:
    print(user.username)
