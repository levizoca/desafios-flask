from flask import Flask, render_template, request, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)

### connect with pymongo ###
app.secret_key = 'super secret key'

client = pymongo.MongoClient("mongodb://%s:%s@localhost:27017/" % ('mongoadmin', 'password'))
db = client["flask-login"]

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

from user import routes

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
