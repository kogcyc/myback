

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://matt:kikikiki@raspberrypi.local/matt'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Sample data
#user = User(username='Matthew')
#db.session.add(user)
#db.session.commit()

# Route
@app.route('/')
def index():
    user = User(username='Anna')
    db.session.add(user)
    db.session.commit()
    all_users = User.query.all()
    #return render_template('index.html', users=all_users)
    ret = {}
    for user in all_users:
    	ret[user.username] = user.username
    return ret

if __name__ == '__main__':
    app.run(debug=True)

