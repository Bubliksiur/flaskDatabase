from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/users')
def users():
    user_list = User.query.all()
    result = "<h1>List of Users</h1>"
    for user in user_list:
        result += f"<p>{user.id}. {user.name} - {user.email}</p>"
    result += '<br><a href="/"><button>Back to Home</button></a>'
    return result

if __name__ == '__main__':
    app.run(debug=True)
