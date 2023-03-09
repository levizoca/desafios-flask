from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required, login_user, logout_user, current_user, LoginForm

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['SECURITY_PASSWORD_SALT'] = 'super-secret-salt'
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask-login',
    'username': 'mongoadmin',
    'password': 'password',
    'host': 'localhost',
    'port': 27017,
}

db = MongoEngine(app)

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    name = db.StringField(max_length=255)
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user = User(name=name, email=email, password=password)
    user.save()
    return redirect('/')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')