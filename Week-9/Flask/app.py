from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
     return render_template('index.html')
# def greet():
    # return render_template('greet.html')

# CONFIGURE THE SQLITE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INITIALIZE DB

db = SQLAlchemy(app)

# CREATE THE USER MODEL

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email_address = db.Column(db.String(80), nullable=False, unique=True)

    def __init__(self, name, age, email_address):
        self.name = name
        self.age = age
        self.email_address = email_address

# CREATE THE DB TABLES
with app.app_context():
    db.create_all()
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#  GET USER INPUT
@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    # ADD A NEW USER TO DB
    new_user = User(name=name, age=age, email_address=email)
    db.session.add(new_user)
    db.session.commit()

    return render_template('hello.html', name=name, email=email, age=age)

@app.route('/users')
def users():
    # DISPLAY ALL USERS
    all_users = User.query.all()
    return render_template('display.html', users=all_users)

if __name__ == '__main__':
    app.run(debug=True)
    