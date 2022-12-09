from app import app, db, login_manager
from flask import render_template
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from forms import RegistrationForm
from models import User

# landing page
@app.route('/')
def index():
    return render_template('index.html')

# registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# *for testing* Users
@app.route('/users')
def user_list():
    current_users = User.query.all()
    return render_template('user_list.html', current_users = current_users)
